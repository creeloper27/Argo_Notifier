#!/usr/bin/env python
# coding: utf-8
"""
	Python API to access to ArgoNext data
	TODO: add comments
"""

# stdlib
import json
import requests
import time

# consts
ARGOAPI_URL="https://www.portaleargo.it/famiglia/api/rest/"
ARGOAPI_KEY="ax6542sdru3217t4eesd9"
ARGOAPI_VERSION="2.0.2"

datGiorno=time.strftime("%Y-%m-%d")


class ArgoUser(object):
	def __init__(self, cod_min, **kwargs):
		super(ArgoUser, self).__init__()
		self.codMin=cod_min
		self.base_header={	"x-cod-min": cod_min,
							"x-key-app": ARGOAPI_KEY,
							"x-version": ARGOAPI_VERSION,
							"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64)\
							AppleWebKit/537.36 (KHTML, like Gecko)\
							Chrome/57.0.2987.133 Safari/537.36"}
		username=kwargs.get("username")
		password=kwargs.get("password")
		token=kwargs.get("token")
		if not (username is None or password is None):
			token=self.login(username, password)
		elif token is None:
			raise ValueError("Not enought parameters to ArgoUser")
		self._token_login(token)
	def login(self, username, password):
		"""
			login with username and password
		"""
		loginheader={"x-user-id": username, "x-pwd": password}

		loginheader.update(self.base_header)
		# return token
		return parse_json(self._request("login", loginheader, {}))["token"]
	def _request(self, page, header, params):
		r=requests.get(
			url=ARGOAPI_URL + page,
			headers=header,
			params=dict(_dc=round(time.time() * 1000), **params)
		)
		if r.status_code != requests.codes.ok:
			raise ConnectionRefusedError("failed to get request [ERROR: "+
										str(r.status_code) + "]")
		return r.text
	def _token_login(self, token):
		token_header = {"x-auth-token": token}
		token_header.update(self.base_header)
		self.userdata=parse_json(self._request("schede", token_header, {}))[0]
		self.base_header=token_header
		self.data_header=dict(	{"x-prg-alunno": str(self.userdata["prgAlunno"]),
								"x-prg-scheda": str(self.userdata["prgScheda"]),
								"x-prg-scuola": str(self.userdata["prgScuola"])},
								**self.base_header)
		self.token=token
	def oggi(self, date=None):
		if date is None:
			date=time.strftime("%Y-%m-%d")
		try:
			data = parse_json(	self._request("oggi",
									self.data_header,
									{"datGiorno": str(date)}
									)
					)
			return data["dati"]
		except ConnectionRefusedError as e:
			return None
	def get(self, attr):
		"""
			get informations from schede
		"""
		try:
			data = parse_json(	self._request(attr,
											self.data_header,
											{"datGiorno": str(time.strftime("%Y-%m-%d"))}
											)
							)
			return data["dati"]
		except ConnectionRefusedError as e:
			return None
	@property
	def assenze(self):
		return self.get("assenze")
	@property
	def noteDisciplinari(self):
		return self.get("notedisciplinari")
	@property
	def votiScrutinio(self):
		return self.get("votiscrutinio")
	@property
	def compiti(self):
		return self.get("compiti")
	@property
	def lezioni(self):
		return self.get("argomenti")
	@property
	def orario(self):
		return self.get("orario")
	@property
	def promemoria(self):
		return self.get("promemoria")
	@property
	def docenti(self):
		return self.get("docenti")

def parse_json(string):
	return json.loads(string)


if __name__ == '__main__':
	"""
		Example of compiti output
		you can give parameters from command line
	"""
	import argparse as arg
	import pprint
	parser=arg.ArgumentParser()
	parser.add_argument("-s", "--schoolcode", dest="schoolcode",
						action="store", required=True)
	parser.add_argument("-u", "--username", dest="username", action="store", default=None)
	parser.add_argument("-p", "--password", dest="password", action="store", default=None)
	parser.add_argument("-t", "--token", dest="token", action="store", default=None)
	parser.add_argument("-f", "--file", dest="file", action="store", default="argo.txt")
	parsed=parser.parse_args()
	argo = ArgoUser(parsed.schoolcode, username=parsed.username,
					password=parsed.password, token=parsed.token)
	f=open(parsed.file, "w+")
	pprint.pprint(argo.compiti, stream=f)
