import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QDialog, QFileDialog

from PyQt5.uic import loadUi


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("gui.ui", self)
        self.browse.clicked.connect(self.browsefiles)

    def browsefiles(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', 'C:', 'Excel Files (*.xlsx)')
        self.filename.setText(fname[0])
        print(fname[0])

app = QApplication(sys.argv)
mainWindow = MainWindow()
winget = QtWidgets.QStackedWidget()

winget.addWidget(mainWindow)
winget.setFixedWidth(400)
winget.setFixedHeight(300)
winget.show()

sys.exit(app.exec_())
