import argoapi
import requests
import json
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QSizePolicy, QSplitter, QDialog, QTableWidgetItem
from PySide2.QtCore import Qt, QSize, Slot
from Main import Ui_MainWindow
from subject_table import Ui_subject_table

debug = 1

class MainWindow(QMainWindow, Ui_MainWindow):
    """docstring for MainWindow."""

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi()
        self.load()

    def setupUi(self):
    	super(MainWindow, self).setupUi(self)
    	self.open_subject_name_button.clicked.connect(self.open_subject_table)

    def load(self):
    	#fa cose dopo aver caricato la finestra
    	pass

    def open_subject_table(self):
    	self.window_subject_table = subject_table(self)
    	self.window_subject_table.show()

class subject_table(QDialog, Ui_subject_table):

	day = ["lunedì","martedì","mercoledì","giovedì","venerdì","sabato","domenica"]

	def __init__(self, parent=None):
		super(subject_table, self).__init__(parent)
		self.setupUi(self)
		self.tableWidget.blockSignals(True);
		self.load()
		self.tableWidget.blockSignals(False);

	def load(self):
		#fa cose dopo aver caricato la finestra
		#per togliere il "?" dalla finestra
		self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
		self.subjects = json.loads(open("subject_table.json", encoding="utf-8").read())
		for x in range(0,7):
			for y in range(0,7):
				if len(self.subjects[self.day[x]])-1>=y:
					if debug:
						print("self.day: {}, x: {}, y: {}, len(self.day[x]): {}, self.subjects[day[x]][y]: {}".format(self.day[x],x,y,len(self.day[x]),self.subjects[self.day[x]][y]))
					self.tableWidget.setItem(y, x, QTableWidgetItem(self.subjects[self.day[x]][y]))

	#edit the subject_table dictionary
	def change_subject_table(self, item):
		if debug:
			print("item: {}\n x: {}, y: {}, text: {}".format(item,item.column(),item.row(),item.text()))
		for i in range(0,item.row()-(len(self.subjects[self.day[item.column()]])-1)):
			self.subjects[self.day[item.column()]].append("")
		if debug:
			print("append*{}, write to: {},{}".format(item.row()-(len(self.subjects[self.day[item.column()]])-1),self.day[item.column()],item.row()))
		self.subjects[self.day[item.column()]][item.row()]=item.text()
	
	#update the new subject_table dictionary to the json
	def update_subject_table(self):
		json.dump(self.subjects, open("subject_table.json", "w+", encoding="utf-8"), indent=4, sort_keys=True)


class MainApp(QApplication):

    def __init__(self, *args, **kwargs):
        super(MainApp, self).__init__(*args, *kwargs)
        #giusto per si mette con self per associarla alla classe anziche alla funzione
        self.window = MainWindow()
        self.window.show()


if __name__ == "__main__":
    app = MainApp(sys.argv)
    sys.exit(app.exec_())


"""

argo = argoapi.ArgoUser("sg18251", username="cattai.lorenzo", password="")

data = argo.compiti

print(data)

print('{} {} {}'.format('Date', 'Subject', 'Content'))
for z in range(1,len(data)):
	print('{} {} {}'.format(data[z]["datGiorno"], data[z]["desMateria"], data[z]["desCompiti"]))
"""



"""
515670434339-qn9t1jorop4ui288olo7tbkei6e0ohtr.apps.googleusercontent.com
UpgEbDEiTjApsYoX24CiQZJH
"""