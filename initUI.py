#Bibliotecas
from __future__ import unicode_literals
import os
from pytube import YouTube, streams
import sys
import youtube_dl
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog
from PyQt5.QtCore import QCoreApplication, QObject, QRunnable


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(200, 40, 325, 347))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.progressBar = QtWidgets.QProgressBar(self.widget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.labelTitulo = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Amarillo")
        font.setPointSize(16)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setObjectName("labelTitulo")
        self.verticalLayout.addWidget(self.labelTitulo)
        self.LinkBaixar = QtWidgets.QLineEdit(self.widget)
        self.LinkBaixar.setObjectName("LinkBaixar")
        self.verticalLayout.addWidget(self.LinkBaixar)
        self.ButtonDownload = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ButtonDownload.setFont(font)
        self.ButtonDownload.setObjectName("ButtonDownload")
        self.verticalLayout.addWidget(self.ButtonDownload)

        self.baixando()

        self.calendarWidget = QtWidgets.QCalendarWidget(self.widget)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelTitulo.setText(_translate("MainWindow", " Baixador YouTube"))
        self.ButtonDownload.setText(_translate("MainWindow", "Download"))
        #self.setGeometry(200, 200, 592, 316)
        #self.setWindowTitle("Youtube Baixador")
        self.font = QtGui.QFont()
        self.font.setFamily("Leelawadee UI")
        #self.std_download_path = str(os.path.join(os.path.expanduser("~"), "Downloads"))
        #self.initUI()
        #self.Ui_MainWindow()

    def baixando(self):
        #self.std_download_path = str(os.path.join(os.path.expanduser("~"), "Downloads"))

        #url = input(str('Link para baixar: '))
        video = YouTube(url)
        stream = video.streams.get_highest_resolution()

        stream.download(output_path='C:/Users/jhonathan.sistema/Desktop')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
