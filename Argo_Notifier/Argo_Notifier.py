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
#QT scheduler IS NOT SUPPORTED WITH PYSIDE2 (but support pyside)
#from apscheduler.schedulers.qt import QtScheduler

debug = 1
settings = json.loads(open("settings.json", encoding="utf-8").read())
subjects = json.loads(open("subject_table.json", encoding="utf-8").read())
scheduler = BackgroundScheduler()

class MainWindow(QMainWindow, Ui_MainWindow):
    """docstring for MainWindow."""

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi()
        self.load()

    def setupUi(self):
    	super(MainWindow, self).setupUi(self)

    def load(self):
    	#fa cose dopo aver caricato la finestra
    	self.start_auto_update()

    def open_subjects_window(self):
        self.window_subjects = SubjectsWindow(self)
        self.window_subjects.show()
        #reflesh subjects, serve per evitare che restino valori non aggiornati sul fine nel dizionario
        subjects = json.loads(open("subject_table.json", encoding="utf-8").read())

    def open_settings_window(self):
        self.window_settings = SettingsWindow(self)
        self.window_settings.show()
        #reflesh subjects, serve per evitare che restino valori non aggiornati sul fine nel dizionario
        settings = json.loads(open("settings.json", encoding="utf-8").read())

    def start_auto_update(self):
        self.update()
        scheduler.add_job(self.update, "interval", minutes=settings["auto_update"]["update_interval"])
        scheduler.start()

    def update(self):
        print("---------Update---------")
        self.update_argo()
        self.update_calendar()

    def update_argo(self):
    	pass

    def update_calendar(self):
    	pass

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
		subjects = json.loads(open("subject_table.json", encoding="utf-8").read())
		for x in range(0,7):
			for y in range(0,7):
				if len(subjects[self.day[x]])-1>=y:
					if debug:
						print("self.day: {}, x: {}, y: {}, len(self.day[x]): {}, subjects[day[x]][y]: {}".format(self.day[x],x,y,len(self.day[x]),subjects[self.day[x]][y]))
					self.tableWidget.setItem(y, x, QTableWidgetItem(subjects[self.day[x]][y]))

	#edit the subject_table dictionary
	def change_subject_table(self, item):
		if debug:
			print("item: {}\n x: {}, y: {}, text: {}".format(item,item.column(),item.row(),item.text()))
		for i in range(0,item.row()-(len(subjects[self.day[item.column()]])-1)):
			subjects[self.day[item.column()]].append("")
		if debug:
			print("append*{}, write to: {},{}".format(item.row()-(len(subjects[self.day[item.column()]])-1),self.day[item.column()],item.row()))
		subjects[self.day[item.column()]][item.row()]=item.text()

	#update the new subject_table dictionary to the json
	def update_subject_table(self):
		json.dump(subjects, open("subject_table.json", "w+", encoding="utf-8"), indent=4, sort_keys=True)

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
		settings = json.loads(open("settings.json", encoding="utf-8").read())
		self.auto_update_interval_spinBox.setValue(settings["auto_update"]["update_interval"])

	#collego tutti i segnali di modifica a questa funzione e updaito settings con tutti i valori correnti
	def change_settings(self):
		settings["auto_update"]["update_interval"]=self.auto_update_interval_spinBox.value()

	def update_settings(self):
		json.dump(settings, open("settings.json", "w+", encoding="utf-8"), indent=4, sort_keys=True)

class MainApp(QApplication):

    def __init__(self, *args, **kwargs):
        super(MainApp, self).__init__(*args, *kwargs)
        #giusto perchè si mette con self per associarla alla classe anziche alla funzione
        self.window = MainWindow()
        self.window.show()


if __name__ == "__main__":
    app = MainApp(sys.argv)
    sys.exit(app.exec_())


"""
argo = argoapi.ArgoUser("sg18251", username="", password="")

data = argo.compiti

print(data)

print('{} {} {}'.format('Date', 'Subject', 'Content'))
for z in range(1,len(data)):
	print('{} {} {}'.format(data[z]["datGiorno"], data[z]["desMateria"], data[z]["desCompiti"]))
"""
