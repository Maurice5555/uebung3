from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.uic import *
import sys
import urllib.parse
from PyQt5.QtGui import *


class UIFenster(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Kapitel 6/showmap.ui", self)
        self.show()

        self.pushButton.clicked.connect(self.buttonclick)

    def buttonclick(self):
        link = f"http://www.google.ch/maps/place/{self.breite.text()},{self.laenge.text()}"
        QDesktopServices.openUrl(QUrl(link))

app=QApplication([])
win=UIFenster()
app.exec()