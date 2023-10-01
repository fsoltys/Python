import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout


class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.stacked = None
        self.setupui()

    def setupui(self):
        self.resize(400, 400)
        layout = QtWidgets.QHBoxLayout(self)
        self.stacked = QtWidgets.QStackedWidget(self)
        layout.addWidget(self.stacked)
        self.setLayout(layout)

        greeting: GreetingScreen = GreetingScreen(self)
        greeting.button.clicked.connect(self.switchview)

        vbox = OtherFunctions(self)

        # index 0  
        self.stacked.addWidget(greeting)
        # index 1
        self.stacked.addWidget(vbox)

        self.stacked.setCurrentWidget(greeting)

        self.show()

    def switchview(self):
        self.stacked.setCurrentIndex(1)


class GreetingScreen(QtWidgets.QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.button = None
        self.label = None
        self.setupui()

    def setupui(self):
        self.resize(400, 400)
        self.label = QtWidgets.QLabel(parent=self, text="Ekran Powitalny")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.button = QtWidgets.QPushButton(parent=self, text="Pokaz inne funkcje")
        layout: QVBoxLayout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.button)


class OtherFunctions(QtWidgets.QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.clearButton = None
        self.UnicodeButton = None
        self.textButton = None
        self.lineEdit = None
        self.label1 = None
        self.label = None
        self.setupui()

    def setupui(self):
        self.resize(400, 400)
        self.label = QtWidgets.QLabel(parent=self, text="Operacje na tekscie")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label1 = QtWidgets.QLabel(parent=self, text="")
        self.lineEdit = QtWidgets.QLineEdit(parent=self)
        self.textButton = QtWidgets.QPushButton(parent=self, text="Wyswietl tekst od tylu")
        self.UnicodeButton = QtWidgets.QPushButton(parent=self, text="Wyswietl tekst jako ciag kodow Unicode")
        self.clearButton = QtWidgets.QPushButton(parent=self, text="Wyczysc pole tekstowe")

        self.textButton.clicked.connect(self.printbackwards)
        self.UnicodeButton.clicked.connect(self.showunicode)
        self.clearButton.clicked.connect(self.clear)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.textButton)
        layout.addWidget(self.UnicodeButton)
        layout.addWidget(self.clearButton)
        layout.addWidget(self.label1)

    def printbackwards(self):
        inputtext = self.lineEdit.text()[::-1]
        self.label1.setText(inputtext)

    def showunicode(self):
        inputtext = self.lineEdit.text()
        result = ""
        for char in inputtext:
            result += str(ord(char))
            result += " "
        self.label1.setText(result)

    def clear(self):
        self.lineEdit.clear()
        self.label1.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    sys.exit(app.exec())
