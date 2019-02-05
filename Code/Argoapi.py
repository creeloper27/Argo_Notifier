#!/usr/bin/env python
# coding: utf-8
"""
Python API to access to ArgoNext data.

See README.md for more informations
"""

import json
import datetime

import requests

__all__ = ("ArgoUser", )

# consts
ARGOAPI_URL = "https://www.portaleargo.com/famiglia/api/rest/"
ARGOAPI_KEY = "ax6542sdru3217t4eesd9"
ARGOAPI_VERSION = "2.0.4"
TODAY = datetime.datetime.today()
TODAY_STR = TODAY.strftime("%Y-%m-%d")


class ArgoUser(object):
    """

    # ArgoUser.

        Represent an Argo user session.
        See README.md for more informations.

    Arguments
    ---------

        schoolcode (required): schoolcode to access to Argo
        username: username to access to Argo
        password: password to access to Argo
        token: you can use it instead of username and password
        full: set "full" parameter of get when you use a class property
    """

    def __init__(self, schoolcode, **kwargs):
        """Init and login into session."""
        super(ArgoUser, self).__init__()
        self.codMin = schoolcode
        self.base_header = {"x-cod-min": schoolcode,
                            "x-key-app": ARGOAPI_KEY,
                            "x-version": ARGOAPI_VERSION,
                            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64)\
                            AppleWebKit/537.36 (KHTML, like Gecko)\
                            Chrome/57.0.2987.133 Safari/537.36"}
        self.full = kwargs.get("full", False)
        username = kwargs.get("username")
        password = kwargs.get("password")
        token = kwargs.get("token")
        if not (username is None or password is None):
            token = self.login(username, password)
        elif token is None:
            raise ValueError("Not enought parameters to ArgoUser")
        self._token_login(token)

    def login(self, username, password):
        """Login with username and password."""
        loginheader = {"x-user-id": username, "x-pwd": password}

        loginheader.update(self.base_header)
        # return token
        return parse_json(self._request("login", loginheader, {}))["token"]

    def _request(self, page, header, params={}):
        """Send requets with header and optionals params to API and return response"."""
        r = requests.get(
            url=ARGOAPI_URL + page,
            headers=header,
            params=params
        )
        if r.status_code != requests.codes.ok:
            raise ConnectionRefusedError("failed to get request [ERROR:{}]".format(r.status_code))
        return r.text

    def _token_login(self, token):
        token_header = {"x-auth-token": token}
        token_header.update(self.base_header)
        self.userdata = parse_json(self._request("schede", token_header, {}))[0]
        self.base_header = token_header
        self.data_header = dict({"x-prg-alunno": str(self.userdata["prgAlunno"]),
                                 "x-prg-scheda": str(self.userdata["prgScheda"]),
                                 "x-prg-scuola": str(self.userdata["prgScuola"])},
                                **self.base_header)
        self.token = token

    def get(self, name):
        """
        Get informations by name.

        It return the json response from API
        """
        try:
            data = parse_json(self._request(name, self.data_header))
            return data
        except ConnectionRefusedError:
            return None

    def oggi(self, date=TODAY_STR):
        """
        Get special property oggi that return the events of the day.

        It provides the same voices as the single properties
        """
        _types = {"COM": "homework", "ARG": "lesson"}
        try:
            data = parse_json(self._request("oggi", self.data_header,
                                            {"datGiorno": date}))
            if self.full:
                return data["dati"]
            else:
                newdata = []
                for el in data:
                    v = el["data"]
                    if el["tipo"] == "COM":
                        newdata.append(dict(type=_types[el["tipo"]],
                                            date=datetime.datetime.strptime(v["datGiorno"], "%Y-%m-%d"),
                                            author=v["docente"][1:-1],
                                            subject=v["desMateria"],
                                            description=v["desCompiti"]))
                    elif el["tipo"] == "ARG":
                        newdata.append(dict(type=_types[el["tipo"]],
                                            date=datetime.datetime.strptime(v["datGiorno"], "%Y-%m-%d"),
                                            author=v["docente"][1:-1],
                                            subject=v["desMateria"],
                                            description=v["desArgomento"]))
                    else:
                        # TODO: find all event types
                        newdata.append(dict(type=None, data=v))
        except ConnectionRefusedError:
            return None

    def orario(self, date=TODAY_STR):
        """
        Get special property orario that return the subjects of the week.

        Non-full data is a 2d matrix sorted by day and hour (in correct order).
        Every voice, which represent an hour, is an array that every element has subject and teacher key.
        If in the voice there isn't any subjects, the voice will be None

        BUG: now Argo API don't provide to select week as the,
            then the date parameter is useless
        """
        try:
            data = parse_json(self._request("orario", self.data_header,
                                            {"datGiorno": date}))
            if self.full:
                return data
            else:
                newdata = []
                daydata = []
                data = data["dati"]
                curgiorno = data[0]["numGiorno"]
                for el in data:
                    if el.get("lezioni") is None:
                        subjects = None
                    else:
                        subjects = []
                        for subject in el["lezioni"]:
                            subject.append(dict(teacher=subject["docente"],
                                                subject=subject["subject"]))
                    if el["numGiorno"] != curgiorno:
                        newdata.append(daydata)
                        daydata = []
                        curgiorno = el["numGiorno"]
                    daydata.append(subjects)

                # XXX: last 2 array can be the same
                newdata.append(daydata)
                return newdata

        except ConnectionRefusedError:
            return None

    @property
    def assenze(self):
        """
        Property to get `assenze` event from argo session.

        Non-full data has these voices:

            type: the type of event. can be E (defferred enter), U (early exit) or A (absence)
            date: the date of event
            hour: the lesson number of event (can be unspecified)
            author: who report the event
            description: optional description of event
            toJustify: if the event have to justify
        """
        data = self.get("assenze")["dati"]
        if self.full:
            return data
        else:
            newdata = []
            for el in data:
                newdata.append(dict(date=datetime.datetime.strptime(el["datAssenza"], "%Y-%m-%d"),
                                    type=el["codEvento"],
                                    hour=el["numOra"],
                                    author=el["registrataDa"][1:-1],
                                    description=el["desAssenza"],
                                    toJustify=el["flgDaGiustificare"]))
            return newdata

    @property
    def noteDisciplinari(self):
        """
        Property to get `noteDisciplinari` event from argo session.

        Non-full data has these voices:

            date: the date of event
            author: who report the event
            description: optional description of event
            isSeen: if the event was seen
        """
        data = self.get("notedisciplinari")["dati"]
        if self.full:
            return data
        else:
            newdata = []
            for el in data:
                newdata.append(dict(date=datetime.datetime.strptime("{} {}".format(el["datNota"],
                                                                                   el.split("oraNota")[1]),
                                                                    "%Y-%m-%d %H:%M"),
                                    author=el["docente"][1:-1],
                                    description=el["desNota"],
                                    isSeen=el["flgVisualizzata"]))
            return newdata

    @property
    def votiGiornalieri(self):
        """
        Property to get `votiGiornalieri` event from argo session.

        Non-full data has these voices:

            type: the type of event. can be S (written test), N (oral interview) or P (practice test)
            date: the date of event
            mark: the evalutation of test in decimal
            author: who report the event
            description: optional description of event
        """
        data = self.get("votigiornalieri")["dati"]
        if self.full:
            return data
        else:
            newdata = []
            for el in data:
                newdata.append(dict(date=datetime.datetime.strptime(el["datGiorno"], "%Y-%m-%d"),
                                    type=el["codVotoPratico"],
                                    mark=el["decValore"],
                                    author=el["docente"][1:-1],
                                    subject=el["desMateria"],
                                    description=el["desCommento"]))
            return newdata

    @property
    def votiScrutinio(self):
        """
        Property to get `VotiScrutinio` event from argo session.

        Non-full data return marks order by interval school report and has these voices:

            name: the name of interval
            marks: list of marks; every marks has these voices:
                subject: mark's subject
                mark: the result of subject in decimal or in words
        """
        def _get_order(obj):
            return d[obj]["order"]
        data = self.get("votiscrutinio")
        if self.full:
            return data
        else:
            newdata = []
            d = {}
            periodi = self.get('periodiclasse')['dati']

            for p in periodi:
                d[p['prgPeriodo']] = dict(name=p['desPeriodo'],
                                          marks=[],
                                          order=p["numOrdine"]
                                          )
            for el in data:
                if el.get("votoAltro") is not None:
                    mark = el.get("votoAltro")['codVoto']
                elif el.get("votoPratico") is not None:
                    mark = el.get("votoPratico")['codVoto']
                elif el.get("votoScritto") is not None:
                    mark = el.get("votoScritto")['codVoto']
                elif el.get("votoOrale") is not None:
                    mark = el.get("votoOrale")['codVoto']
                else:
                    mark = None

                d[el["prgPeriodo"]]["marks"].append(dict(subject=el["desMateria"], mark=mark))

            for y in sorted(d, key=_get_order):
                d[y].pop("order", None)
                newdata.append(d[y])

            return newdata

    @property
    def compiti(self):
        """
        Property to get "compiti" event from argo session.

        Non-full data has these voices:

            date: the date of event
            description: optional description of event
            subject: the subject of the event
            author: who report the event
        """
        data = self.get("compiti")["dati"]
        if self.full:
            return data
        else:
            newdata = []
            for el in data:
                newdata.append(dict(date=datetime.datetime.strptime(el["datGiorno"], "%Y-%m-%d"),
                                    author=el["docente"][1:-1],
                                    subject=el["desMateria"],
                                    description=el["desCompiti"]))
            return newdata

    @property
    def lezioni(self):
        """
        Property to get "lezioni" event from argo session.

        Non-full data has these voices:

            date: the date of event
            description: optional description of event
            subject: the subject of the event
            author: who report the event
        """
        data = self.get("argomenti").get("dati", {})
        if self.full:
            return data
        else:
            newdata = []
            for el in data:
                newdata.append(dict(date=datetime.datetime.strptime(el["datGiorno"], "%Y-%m-%d"),
                                    author=el["docente"][1:-1],
                                    subject=el["desMateria"],
                                    description=el["desArgomento"]))
            return newdata

    @property
    def docenti(self):
        """
        Property to get "docenti" event from argo session.

        Non-full data has these voices:

            name: the name of teacher
            surname: the surname of teacher
            email: the email of teacher, if he haven't, is None
            subject: the subject of the event
        """
        data = self.get("docenticlasse")
        if self.full:
            return data
        else:
            newdata = []
            for el in data:
                newdata.append(dict(name=el['docente']['nome'],
                                    surname=el['docente']['cognome'],
                                    email=el['docente']['email'] if el['docente']['nome'] != el['docente']['email'] else None,
                                    subject=el['materie'][1:-1].split(' ,')
                                    ))
            return newdata

    @property
    def bacheca(self):
        """
        Property to get "backeca" event from argo session.

        Non-full data has these voices:

            date: the date of event
            title: the topic of event
            description: optional description of event
            attachment: optional attachment of the event, can contain file, raw file or an url
        """
        data = self.get("bacheca")["dati"]
        if self.full:
            return data
        else:
            newdata = []
            for el in data:
                attachment = {}
                if el.get("desFile") is not None:
                    attachment["file"] = el["desFile"]
                if el.get("desFileFisico") is not None:
                    attachment["rawfile"] = el["desFileFisico"]
                if el.get("desUrl") is not None:
                    attachment["url"] = el["desUrl"]

                newdata.append(dict(date=datetime.datetime.strptime(el["datGiorno"], "%Y-%m-%d"),
                                    title=el["desOggetto"],
                                    description=el["desMessaggio"],
                                    attachment=attachment))
            return newdata

    @property
    def promemoria(self):
        """
        Property to get "promemoria" event from argo session.

        Non-full data has these voices:

            date: the date of event
            description: optional description of event
            author: who report the event
        """
        data = self.get("promemoria").get("dati", {})
        if self.full:
            return data
        else:
            newdata = []
            for el in data:
                newdata.append(dict(date=datetime.datetime.strptime(el["datGiorno"], "%Y-%m-%d"),
                                    author=el["desMittente"][1:-1],
                                    description=el["desAnnotazioni"]))
            return newdata


def parse_json(string):
    return json.loads(string)


if __name__ == '__main__':
    """
        Save page informations
    """
    import argparse as arg
    parser = arg.ArgumentParser()
    parser.add_argument("-s", "--schoolcode", dest="schoolcode",
                        action="store", required=True)
    parser.add_argument("-u", "--username", dest="username", action="store", default=None)
    parser.add_argument("-p", "--password", dest="password", action="store", default=None)
    parser.add_argument("-t", "--token", dest="token", action="store", default=None)
    parser.add_argument("-f", "--file", dest="file", action="store", default="argo.json")
    parser.add_argument("--page", dest="page", action="store", default="compiti")
    parser.add_argument("--full", dest="full", action="store_true", default=False)
    parsed = parser.parse_args()
    argo = ArgoUser(parsed.schoolcode, username=parsed.username,
                    password=parsed.password, token=parsed.token, full=parsed.full)

    f = open(parsed.file, "w+")
    if parsed.page in ("orario", "oggi"):
        json.dump(getattr(argo, parsed.page,
                          {"error": "Property {} not found".format(parsed.page)})("2018-03-14"), f,
                  indent=4, sort_keys=True)
    else:
        json.dump(getattr(argo, parsed.page,
                          {"error": "Property {} not found".format(parsed.page)}), f,
                  indent=4, sort_keys=True)
