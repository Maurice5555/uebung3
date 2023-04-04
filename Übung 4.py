import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.createLayout()
        self.createConnects()

    def createLayout(self):
       
        self.setWindowTitle("GUI-Programmierung")

        layout = QFormLayout()

        self.vornameLineEdit = QLineEdit()
        self.nameLineEdit = QLineEdit()
        self.geburtstagLineEdit = QDateEdit()
        self.adresseLIneEdit = QLineEdit()
        self.postleitzahlLineEdit = QLineEdit()
        self.ortLineEdit = QLineEdit()
        self.land = QComboBox()
        self.land.addItems(["Schweiz", "Deutschland", "Österreich"])
        self.savebutton = QPushButton("Save")

        layout.addRow("Vorname:", self.vornameLineEdit)
        layout.addRow("Name:", self.nameLineEdit)
        layout.addRow("Geburtstag:", self.geburtstagLineEdit)
        layout.addRow("Adresse:", self.adresseLIneEdit)
        layout.addRow("PostLeitzahl:", self.postleitzahlLineEdit)
        layout.addRow("Ort:", self.ortLineEdit)
        layout.addRow("Land:", self.land)
        layout.addRow(self.savebutton)

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

        self.show()

        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")

        save = QAction("Save", self)
        quit = QAction("Quit", self)

        filemenu.addAction(save)
        filemenu.addAction(quit)

        quit.triggered.connect(self.quitbutton_clicked)
        save.triggered.connect(self.speichern)

    def quitbutton_clicked(self):
        self.close()

    def createConnects(self):
        self.savebutton.clicked.connect(self.speichern)

    def speichern(self):
        file = open("output.txt", "w")
        file.write(f"{self.vornameLineEdit.text()}, {self.nameLineEdit.text()}, {self.geburtstagLineEdit.text()}, {self.adresseLIneEdit.text()}, {self.postleitzahlLineEdit.text()}, {self.ortLineEdit.text()}, {self.land.currentText()}")
        file.close()
        
        print(self.vornameLineEdit.text())
def main():
    app = QApplication(sys.argv)  
    mainwindow = MyWindow()       
    mainwindow.raise_()           
    app.exec_()                   

if __name__ == '__main__':
    main()