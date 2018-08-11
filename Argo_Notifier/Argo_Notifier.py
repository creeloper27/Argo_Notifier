import argoapi
import requests
import json
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QSizePolicy, QSplitter, QMessageBox
from PySide2.QtCore import Qt, QSize
from Main import Ui_MainWindow
from subject_table import Ui_Dialog


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
    	self.window_subject_table = subject_table()
    	self.window_subject_table.show()

class subject_table(QMessageBox, Ui_Dialog):

	def __init__(self, parent=None):
		super(subject_table, self).__init__(parent)
		self.setupUi(self)
		self.load()

	def load(self):
		#fa cose dopo aver caricato la finestra
		subjects = json.load("subject_table.json")
		"""for x in range(1,7)
				for y in range(1,7)
				setItem(0, 1, new QTableWidgetItem("Hello"))"""
		

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