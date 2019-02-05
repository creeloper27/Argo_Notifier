#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import json
import datetime
import Argoapi

from apscheduler.schedulers.background import BackgroundScheduler
from PySide2.QtCore import Qt, QSize, Slot
from PySide2.QtWidgets import QApplication, QMainWindow, QSizePolicy, QSplitter, QDialog, QTableWidgetItem
from googleapiclient.discovery import build
from oauth2client import file, client, tools
from httplib2 import Http

# this is needed because they are in a different folder
sys.path.insert(0, '../QtWindows')
from SettingsWindow import Ui_SettingsWindow
from SubjectsWindow import Ui_SubjectsWindow
from Main import Ui_MainWindow

# from apscheduler.schedulers.qt import QtScheduler
# QT scheduler IS NOT SUPPORTED WITH PYSIDE2 (but it is with pyside)
# becuase of this i'm using backgroundscheduler


class MainWindow(QMainWindow, Ui_MainWindow):
    """docstring for MainWindow."""

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        super(MainWindow, self).setupUi(self)

    def load(self):
        # fa cose dopo aver caricato la finestra
        self.start_auto_update()

    def open_subjects_window(self):
        self.window_subjects = SubjectsWindow(self)
        self.window_subjects.show()
        # reflesh subjects, serve per evitare che restino valori non aggiornati sul fine nel dizionario
        app.subjects = json.loads(
            open("../Data/subject_table.json", encoding="utf-8").read())

    def open_settings_window(self):
        self.window_settings = SettingsWindow(self)
        self.window_settings.show()
        # reflesh subjects, serve per evitare che restino valori non aggiornati sul fine nel dizionario
        app.settings = json.loads(
            open("../Data/settings.json", encoding="utf-8").read())

    def start_auto_update(self):
        self.update()
        app.current_auto_update_interval = app.settings["auto_update"]["update_interval"]
        app.auto_update_job = app.scheduler.add_job(
            app.update, "interval", minutes=app.settings["auto_update"]["update_interval"])
        app.scheduler.start()

    def app_update(self):
        app.update()


class SubjectsWindow(QDialog, Ui_SubjectsWindow):

    def __init__(self, parent=None):
        super(SubjectsWindow, self).__init__(parent)
        self.setupUi(self)
        self.tableWidget.blockSignals(True)
        self.load()
        self.tableWidget.blockSignals(False)

    def load(self):
        # fa cose dopo aver caricato la finestra
        # per togliere il "?" dalla finestra
        self.setWindowFlags(self.windowFlags() & ~
                            Qt.WindowContextHelpButtonHint)
        app.subjects = json.loads(
            open("../Data/subject_table.json", encoding="utf-8").read())
        for x in range(0, 7):
            for y in range(0, 7):
                if len(app.subjects[app.day[x]]) - 1 >= y:
                    if app.debug:
                        print("app.day: {}, x: {}, y: {}, len(app.day[x]): {}, app.subjects[app.day[x]][y]: {}".format(
                            app.day[x], x, y, len(app.day[x]), app.subjects[app.day[x]][y]))
                    self.tableWidget.setItem(
                        y, x, QTableWidgetItem(app.subjects[app.day[x]][y]))

    # edit the subject_table dictionary
    def change_subject_table(self, item):
        if app.debug:
            print("item: {}\n x: {}, y: {}, text: {}".format(
                item, item.column(), item.row(), item.text()))
        for i in range(0, item.row() - (len(app.subjects[app.day[item.column()]]) - 1)):
            app.subjects[app.day[item.column()]].append("")
        if app.debug:
            print("append*{}, write to: {},{}".format(item.row() -
                                                      (len(app.subjects[app.day[item.column()]]) - 1), app.day[item.column()], item.row()))
        app.subjects[app.day[item.column()]][item.row()] = item.text()

    # update the new subject_table dictionary to the json
    def update_subject_table(self):
        json.dump(app.subjects, open("../Data/subject_table.json", "w+",
                                     encoding="utf-8"), indent=4, sort_keys=True)


class SettingsWindow(QDialog, Ui_SettingsWindow):
    def __init__(self, parent=None):
        super(SettingsWindow, self).__init__(parent)
        self.setupUi(self)
        # FIXARE BLOCK SIGNALS PER TUTTI I WIDGET (self.block non credo vada)
        self.blockSignals(True)
        self.load()
        self.blockSignals(False)

    def load(self):
        # fa cose dopo aver caricato la finestra
        # per togliere il "?" dalla finestra
        self.setWindowFlags(self.windowFlags() & ~
                            Qt.WindowContextHelpButtonHint)
        app.settings = json.loads(
            open("../Data/settings.json", encoding="utf-8").read())
        self.auto_update_interval_spinBox.setValue(
            app.settings["auto_update"]["update_interval"])

    # collego tutti i segnali di modifica a questa funzione e updaito settings con tutti i valori correnti
    def change_settings(self):
        app.settings["auto_update"]["update_interval"] = self.auto_update_interval_spinBox.value()

    def update_settings(self):
        if app.debug:
            print("before update:")
            app.scheduler.print_jobs()
        if (app.current_auto_update_interval != app.settings["auto_update"]["update_interval"]):
            if app.debug:
                print("edit to update_interval: {}->{}".format(app.current_auto_update_interval,
                                                               app.settings["auto_update"]["update_interval"]))
            app.auto_update_job.remove()
            app.auto_update_job = app.scheduler.add_job(
                app.update, "interval", minutes=app.settings["auto_update"]["update_interval"])
        if app.debug:
            print("after update:")
            app.scheduler.print_jobs()
        json.dump(app.settings, open("../Data/settings.json", "w+",
                                     encoding="utf-8"), indent=4, sort_keys=True)


class MainApp(QApplication):

    def __init__(self, *args, **kwargs):
        self.debug = True
        try:
            self.settings = json.loads(
                open("../Data/settings.json", encoding="utf-8").read())
            self.subjects = json.loads(
                open("../Data/subject_table.json", encoding="utf-8").read())
            self.argo_credentials = json.loads(
                open("../Data/Credentials/argo_credentials.json", encoding="utf-8").read())
            self.argo_token = json.loads(
                open("../Data/Credentials/argo_token.json", encoding="utf-8").read())
            self.calendar_credentials = json.loads(
                open("../Data/Credentials/calendar_credentials.json", encoding="utf-8").read())
            self.calendar_token = json.loads(
                open("../Data/Credentials/calendar_token.json", encoding="utf-8").read())
        except FileNotFoundError as e:
            print(e)
            print("File Not Found")

        self.day = ["lunedì", "martedì", "mercoledì",
                    "giovedì", "venerdì", "sabato", "domenica"]
        self.scheduler = BackgroundScheduler()
        self.auto_update_job = None
        self.current_auto_update_interval = None
        self.tests = None

        super(MainApp, self).__init__(*args, *kwargs)
        self.window = MainWindow()

    def load(self):
        self.window.load()

    def show(self):
        self.window.show()

    def update(self):
        print("---------Update---------")
        self.tests = self.update_argo()
        # aggiungo il giorno ai dizionary dei test
        for test in self.tests:
            if test["subject"] == "Lab.-tec.sist.i&t":
                test["subject"] = "Tecnologie e progettazione sistemi informatici e telecom."
            if test["subject"] == "Lab.-informatica":
                test["subject"] = "Informatica"
            if test["subject"] == "Lab.-sistemi":
                test["subject"] = "Sistemi e reti"

            test["day"] = app.day[test["date"].weekday()]
        if self.debug:
            # non ha senso
            print('| {} | {} | {} | {} |\n'.format(
                'Date', 'Day', 'Subject', 'Description'))
            for z in range(0, len(self.tests)):
                print('| {} | {} | {} | {} |'.format(
                    self.tests[z]["date"], self.tests[z]["day"], self.tests[z]["subject"], self.tests[z]["description"].replace("\n", " ")))

        self.update_calendar(self.tests)

    def update_argo(self):
        if self.argo_token:
            argo = Argoapi.ArgoUser(schoolcode=self.argo_credentials["school_code"],
                                    token=self.argo_token["token"])
        elif self.argo_credentials:
            argo = Argoapi.ArgoUser(schoolcode=self.argo_credentials["school_code"],
                                    username=self.argo_credentials["username"],
                                    password=self.argo_credentials["password"])
        else:
            raise SthWentWrong("Something went wrong :(")

        tests = self.filter_tests(argo.compiti)
        return tests

    def filter_tests(self, data):
        """Filter data to get all tests using AAFT (Advanced Algorithm For detecting Tests)."""
        tests = []
        for homework in data:
            description = homework["description"]
            # creare algoritmo per individuare la descrizione della verifica e separarla dal resto, etc.
            if (((description.lower().find("verifica") != -1) or (description.lower().find("compito") != -1)) and (description.lower().find("recupero") == -1) and (description.lower().find("autoverifica") == -1) and (description.lower().find("previsione") == -1)):
                tests.append({"date": homework["date"], "day": None,
                              "subject": homework["subject"], "description": homework["description"]})
        return tests

    def update_calendar(self, tests):
        SCOPES = 'https://www.googleapis.com/auth/calendar'
        store = file.Storage('Data/Credentials/calendar_token.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets(
                'Data/Credentials/calendar_credentials.json', SCOPES)
            creds = tools.run_flow(flow, store)
        service = build('calendar', 'v3', http=creds.authorize(Http()))

        for test in tests:
            try:
                start_hour, end_hour = app.subjects["orari"][app.subjects[test["day"]].index(
                    test["subject"])]
                strdate = test["date"].strftime("%Y-%m-%d-")
                start = datetime.datetime.strptime(strdate + start_hour,
                                                   "%Y-%m-%d-%H-%M").isoformat() + 'Z'
                end = datetime.datetime.strptime(strdate + end_hour,
                                                 "%Y-%m-%d-%H-%M").isoformat() + 'Z'
                if app.debug:
                    print("\nStart: ", start, "End: ", end)
                events_result = service.events().list(calendarId='primary', timeMin=start, timeMax=end,
                                                      singleEvents=True, maxResults=10,
                                                      orderBy='startTime').execute()
                events = events_result.get('items', [])

                if not events:
                    print('-----No events found-----')
                    # add event
                    # you can attach files, and so much more!
                    # https://developers.google.com/calendar/create-events
                    event = {
                        'summary': "Verifica di {}".format(test["subject"]),
                        # da cambiare in futuro
                        'description': test["description"],
                        'start': {
                            'dateTime': start,
                        },
                        'end': {
                            'dateTime': end,
                        }
                    }

                    event = service.events().insert(calendarId='primary', body=event).execute()
                    print('Event created: %s' % (event.get('htmlLink')))
                else:
                    print('-----Events found-----')
                    # show event that is already there
                    for event in events:
                        start = event['start'].get(
                            'dateTime', event['start'].get('date'))
                    print(start, event['summary'])

            except Exception as e:
                print("Subject not found", e)
                raise e


if __name__ == "__main__":
    app = MainApp(sys.argv)
    app.load()
    app.show()
    sys.exit(app.exec_())
