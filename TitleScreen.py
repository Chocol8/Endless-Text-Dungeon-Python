# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TitleScreen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QDialogButtonBox, QLabel, QMainWindow, QMessageBox, QPushButton, QVBoxLayout
import sys
import os

class Ui_TitleScreen(object):
    def ContinueGameWindow(self):
        if(os.path.exists('save.txt') == True):
            from uiLoad import Ui_LoadGameWindow
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_LoadGameWindow()
            self.ui.setupUi(self.window)
            self.window.show()    
        else:
            message = QMessageBox.critical(TitleScreen,"ERROR","There is no save")
            if message:
                TitleScreen.show()

    def EnterName(self):
        global name 
        from ui import Ui_GameWindow
        name, ok = QtWidgets.QInputDialog.getText(TitleScreen, 'Name Input','Enter your name:')
        if ok:
            if(len(name)==0):
                name = "Hero"
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_GameWindow()
            self.ui.setupUi(self.window)
            self.window.show()
            self.ui.PlayerName.setText(name)
            save = open('save.txt','w')
            save.write(name)
            save.close()

    def ExitGame(self):
        question = QMessageBox.question(TitleScreen, "Exit Game?", "Are you sure you want to exit the game?")
        if question == QMessageBox.Yes:
            TitleScreen.close()

    def setupUi(self, TitleScreen):
        self.TitleScreen = TitleScreen
        TitleScreen.setObjectName("TitleScreen")
        TitleScreen.resize(600, 391)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TitleScreen.sizePolicy().hasHeightForWidth())
        TitleScreen.setSizePolicy(sizePolicy)
        TitleScreen.setMinimumSize(QtCore.QSize(600, 391))
        TitleScreen.setMaximumSize(QtCore.QSize(600, 391))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/zjbar/Documents/NetBeansProjects/FinalProj/Image/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TitleScreen.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(TitleScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 130, 147, 48))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)

        #newgame
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("New_Game")
        self.pushButton.clicked.connect(self.EnterName)
        self.pushButton.clicked.connect(TitleScreen.close)
        

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 531, 61))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        '''
        continue
        '''
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 190, 147, 48))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("continue")
        self.pushButton_2.clicked.connect(self.ContinueGameWindow)
        self.pushButton_2.clicked.connect(TitleScreen.close)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 250, 147, 48))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)

        #exitgame
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("exitgame")
        self.pushButton_3.clicked.connect(self.ExitGame)

        TitleScreen.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(TitleScreen)
        self.statusbar.setObjectName("statusbar")
        TitleScreen.setStatusBar(self.statusbar)

        self.retranslateUi(TitleScreen)
        QtCore.QMetaObject.connectSlotsByName(TitleScreen)

    def retranslateUi(self, TitleScreen):
        _translate = QtCore.QCoreApplication.translate
        TitleScreen.setWindowTitle(_translate("TitleScreen", "Endless Text Dungeon"))
        self.pushButton.setText(_translate("TitleScreen", "Enter"))
        self.label.setText(_translate("TitleScreen", "Welcome to Endless Text Dungeon!"))
        self.pushButton_2.setText(_translate("TitleScreen", "Continue"))
        self.pushButton_3.setText(_translate("TitleScreen", "Exit"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    TitleScreen = QtWidgets.QMainWindow()
    ui = Ui_TitleScreen()
    ui.setupUi(TitleScreen)
    TitleScreen.show()
    sys.exit(app.exec_())

