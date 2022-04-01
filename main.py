#Programa para fazer download de videos do youtube

#Bibliotecas
from __future__ import unicode_literals
import os
import sys
import youtube_dl
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog
from PyQt5.QtCore import QCoreApplication, QObject, QRunnable

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(200, 200, 592, 316)
        self.setWindowTitle("Youtube Baixador")
        self.font = QtGui.QFont()
        self.font.setFamily("Leelawadee UI")
        self.std_download_path = str(os.path.join(os.path.expanduser("~"), "Downloads"))
        self.initUI()


