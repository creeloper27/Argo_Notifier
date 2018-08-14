#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argoapi
import requests
import json
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QSizePolicy, QSplitter, QDialog, QTableWidgetItem
from PySide2.QtCore import Qt, QSize, Slot
from Main import Ui_MainWindow
from SubjectsWindow import Ui_SubjectsWindow
from SettingsWindow import Ui_SettingsWindow
from apscheduler.schedulers.background import BackgroundScheduler
#QT scheduler IS NOT SUPPORTED WITH PYSIDE2 (but support pyside) so i'm using backgroundscheduler
#from apscheduler.schedulers.qt import QtScheduler


class MainWindow(QMainWindow, Ui_MainWindow):
	"""docstring for MainWindow."""

	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setupUi()

	def setupUi(self):
		super(MainWindow, self).setupUi(self)

	def load(self):
		#fa cose dopo aver caricato la finestra
		self.start_auto_update()

	def open_subjects_window(self):
		self.window_subjects = SubjectsWindow(self)
		self.window_subjects.show()
		#reflesh subjects, serve per evitare che restino valori non aggiornati sul fine nel dizionario
		app.subjects = json.loads(open("subject_table.json", encoding="utf-8").read())

	def open_settings_window(self):
		self.window_settings = SettingsWindow(self)
		self.window_settings.show()
		#reflesh subjects, serve per evitare che restino valori non aggiornati sul fine nel dizionario
		app.settings = json.loads(open("settings.json", encoding="utf-8").read())

	def start_auto_update(self):
		self.update()
		app.current_auto_update_interval=app.settings["auto_update"]["update_interval"]
		app.auto_update_job = app.scheduler.add_job(app.update, "interval", minutes=app.settings["auto_update"]["update_interval"])
		app.scheduler.start()

class SubjectsWindow(QDialog, Ui_SubjectsWindow):

	day = ["lunedì","martedì","mercoledì","giovedì","venerdì","sabato","domenica"]

	def __init__(self, parent=None):
		super(SubjectsWindow, self).__init__(parent)
		self.setupUi(self)
		self.tableWidget.blockSignals(True);
		self.load()
		self.tableWidget.blockSignals(False);

	def load(self):
		#fa cose dopo aver caricato la finestra
		#per togliere il "?" dalla finestra
		self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
		app.subjects = json.loads(open("subject_table.json", encoding="utf-8").read())
		for x in range(0,7):
			for y in range(0,7):
				if len(app.subjects[self.day[x]])-1>=y:
					if app.debug:
						print("self.day: {}, x: {}, y: {}, len(self.day[x]): {}, app.subjects[day[x]][y]: {}".format(self.day[x],x,y,len(self.day[x]),app.subjects[self.day[x]][y]))
					self.tableWidget.setItem(y, x, QTableWidgetItem(app.subjects[self.day[x]][y]))

	#edit the subject_table dictionary
	def change_subject_table(self, item):
		if app.debug:
			print("item: {}\n x: {}, y: {}, text: {}".format(item,item.column(),item.row(),item.text()))
		for i in range(0,item.row()-(len(app.subjects[self.day[item.column()]])-1)):
			app.subjects[self.day[item.column()]].append("")
		if app.debug:
			print("append*{}, write to: {},{}".format(item.row()-(len(app.subjects[self.day[item.column()]])-1),self.day[item.column()],item.row()))
		app.subjects[self.day[item.column()]][item.row()]=item.text()

	#update the new subject_table dictionary to the json
	def update_subject_table(self):
		json.dump(app.subjects, open("subject_table.json", "w+", encoding="utf-8"), indent=4, sort_keys=True)

class SettingsWindow(QDialog, Ui_SettingsWindow):
	def __init__(self, parent=None):
		super(SettingsWindow, self).__init__(parent)
		self.setupUi(self)
		#FIXARE BLOCK SIGNALS PER TUTTI I WIDGET (self.block non credo vada)
		self.blockSignals(True);
		self.load()
		self.blockSignals(False);

	def load(self):
		#fa cose dopo aver caricato la finestra
		#per togliere il "?" dalla finestra
		self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
		app.settings = json.loads(open("settings.json", encoding="utf-8").read())
		self.auto_update_interval_spinBox.setValue(app.settings["auto_update"]["update_interval"])

	#collego tutti i segnali di modifica a questa funzione e updaito settings con tutti i valori correnti
	def change_settings(self):
		app.settings["auto_update"]["update_interval"]=self.auto_update_interval_spinBox.value()

	def update_settings(self):
		if app.debug:
			print("before update:")
			app.scheduler.print_jobs()
		if (app.current_auto_update_interval!=app.settings["auto_update"]["update_interval"]):
			if app.debug:
				print("edit to update_interval: {}->{}".format(app.current_auto_update_interval,app.settings["auto_update"]["update_interval"]))
			app.auto_update_job.remove()
			app.auto_update_job = app.scheduler.add_job(app.update, "interval", minutes=app.settings["auto_update"]["update_interval"])
		if app.debug:
			print("after update:")
			app.scheduler.print_jobs()
		json.dump(app.settings, open("settings.json", "w+", encoding="utf-8"), indent=4, sort_keys=True)

class MainApp(QApplication):

	def __init__(self, *args, **kwargs):
		self.debug = True
		self.settings = json.loads(open("settings.json", encoding="utf-8").read())
		self.subjects = json.loads(open("subject_table.json", encoding="utf-8").read())
		self.scheduler = BackgroundScheduler()
		self.auto_update_job = None
		self.current_auto_update_interval = None


		super(MainApp, self).__init__(*args, *kwargs)
		self.window = MainWindow()

	def load(self):
		self.window.load()

	def show(self):
		self.window.show()

	def update(self):
		print("---------Update---------")
		self.update_argo()
		self.update_calendar()
	def update_argo(self):
		pass

	def update_calendar(self):
		pass

if __name__ == "__main__":
	app = MainApp(sys.argv)
	app.load()
	app.show()
	sys.exit(app.exec_())


"""
argo = argoapi.ArgoUser("sg18251", username="", password="")

data = argo.compiti

print(data)

print('{} {} {}'.format('Date', 'Subject', 'Content'))
for z in range(1,len(data)):
	print('{} {} {}'.format(data[z]["datGiorno"], data[z]["desMateria"], data[z]["desCompiti"]))
"""
