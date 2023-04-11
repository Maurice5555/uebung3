import sys
import urllib.parse
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.createLayout()
        self.createConnects()

    def createLayout(self):
       
        self.setWindowTitle("GUI-Programmierung")

        layout = QFormLayout()
        layoutadd = QHBoxLayout()

        self.vornameLineEdit = QLineEdit()
        self.nameLineEdit = QLineEdit()
        self.geburtstagLineEdit = QDateEdit()
        self.strasseLineEdit = QLineEdit()
        self.nummerLineEdit = QLineEdit()
        self.postleitzahlLineEdit = QLineEdit()
        self.ortLineEdit = QLineEdit()
        self.land = QComboBox()
        self.land.addItems(["Schweiz", "Deutschland", "Österreich"])
        self.aufkarteanzeigen = QPushButton("Auf Karte Anzeigen")
        self.laden = QPushButton("Laden")
        self.savebutton = QPushButton("Save")

        layout.addRow("Vorname:", self.vornameLineEdit)
        layout.addRow("Name:", self.nameLineEdit)
        layout.addRow("Geburtstag:", self.geburtstagLineEdit)
        layout.addRow("Adresse:", layoutadd)
        layout.addRow("PostLeitzahl:", self.postleitzahlLineEdit)
        layout.addRow("Ort:", self.ortLineEdit)
        layout.addRow("Land:", self.land)
        layout.addRow(self.aufkarteanzeigen)
        layout.addRow(self.laden)
        layout.addRow(self.savebutton)

        layoutadd.addWidget(self.strasseLineEdit)
        layoutadd.addWidget(self.nummerLineEdit)

        self.aufkarteanzeigen.clicked.connect(self.mapple)
        self.laden.clicked.connect(self.openup)
        self.savebutton.clicked.connect(self.save)

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

        self.show()

        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        viewmenu = menubar.addMenu("View")

        save = QAction("Save", self)
        quit = QAction("Quit", self)
        open = QAction("Laden", self)
        map = QAction("Karte", self)

        filemenu.addAction(save)
        filemenu.addAction(quit)
        filemenu.addAction(open)
        viewmenu.addAction(map)

        quit.triggered.connect(self.quitbutton_clicked)
        save.triggered.connect(self.save)
        open.triggered.connect(self.openup)
        map.triggered.connect(self.mapple)

    def quitbutton_clicked(self):
        self.close()

    def openup(self):
        
        filename, filter = QFileDialog.getOpenFileName(self, "Datei öffnen", "C:/", "Python Files (*.py) ;; Text Files (*.txt)")

        if filename !="":
            print(filename)
        else:
            print("Abgebrochen")

    def mapple(self):
        link = f"http://www.google.ch/maps/place/{self.strasseLineEdit.text()}+{self.nummerLineEdit.text()}+{self.postleitzahlLineEdit.text()}+{self.ortLineEdit.text()}+{self.land.currentText()}"
        QDesktopServices.openUrl(QUrl(link))   # benötigt QtCore & QtGui
        #https://www.google.ch/maps/place/Hofackerstrasse+30+4132+Muttenz+Schweiz

    def createConnects(self):
        self.savebutton.clicked.connect(self.save)
        self.laden.clicked.connect(self.openup)

    def save(self):
        filename, filter = QFileDialog.getSaveFileName(self, "Datei speichern", "", "Text Datei (*.txt)")
        print(filename)

def main():
    app = QApplication(sys.argv)  
    mainwindow = MyWindow()       
    mainwindow.raise_()           
    app.exec_()                   

if __name__ == '__main__':
    main()