# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Game.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from os import name
from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5
from PyQt5.QtWidgets import QApplication, QDialog, QDialogButtonBox, QLabel, QMainWindow, QMessageBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import sys
import random

#Variables
MinAtk = [7, 1, 4, 3, 1, 1, 5, 3, 1, 1, 5, 4, 10, 13, 15, 10, 7, 15, 15, 7]
MaxAtk = [12, 6, 7, 6, 6, 6, 8, 6, 8, 6, 7, 6, 20, 15, 20, 15, 10, 22, 25, 12]
Enum = 1 #EnemyNumber

class GameProper(QWidget):
    def __init__(this,Enum,Defeated,HPPlayer,HPEnemy,EnemyName,PlayerName,MaxHPPlayer,MaxHPEnemy):
        this.Enum = Enum
        this.Defeated = Defeated
        this.HPPlayer = HPPlayer
        this.HPEnemy = HPEnemy
        this.EnemyName = EnemyName
        this.PlayerName = PlayerName
        this.MaxHPPlayer = MaxHPPlayer
        this.MaxHPEnemy = MaxHPEnemy
    def EnemyRoll(this,self):
        Roll = random.randint(1,100)
        if(this.Defeated >=10 and ((this.Defeated % 10) == 0)):
            if (this.Defeated >= 30 and ((this.Defeated % 30) == 0)):
                self.textBrowser.append("You encountered a Doppelganger")
                this.EnemyName = "Doppelganger"
                self.EnemyName.setText(this.EnemyName)
                this.HPEnemy = 100
                this.MaxHPEnemy = 100
                self.EnemyHealth.setText(str(this.HPEnemy)+'/'+str(this.MaxHPEnemy))
                this.Enum = 19

            else:
                if(Roll <= 15):
                    self.textBrowser.append('You encountered a Spider Broodmother')
                    this.EnemyName = "Spooder Brod."
                    self.EnemyName.setText(this.EnemyName)
                    this.HPEnemy = 45
                    this.MaxHPEnemy = 45
                    self.EnemyHealth.setText(str(this.HPEnemy)+'/'+str(this.MaxHPEnemy))
                    this.Enum = 12

                elif(Roll > 15 and Roll <= 29):
                    self.textBrowser.append('You encountered a Vampire Lord')
                    this.EnemyName = "Vampire Lord"
                    self.EnemyName.setText(this.EnemyName)
                    this.HPEnemy = 60
                    this.MaxHPEnemy = 60
                    self.EnemyHealth.setText(str(this.HPEnemy)+'/'+str(this.MaxHPEnemy))
                    this.Enum = 13
                elif(Roll > 29 and Roll <= 44):
                    self.textBrowser.append('You encountered a T. Rex')
                    this.EnemyName = "T. Rex"
                    self.EnemyName.setText(this.EnemyName)
                    this.HPEnemy = 45
                    this.MaxHPEnemy = 45
                    self.EnemyHealth.setText(str(this.HPEnemy)+'/'+str(this.MaxHPEnemy))
                    this.Enum = 14
                elif(Roll > 44 and Roll <= 59):
                    self.textBrowser.append('You encountered a Gorgon')
                    this.EnemyName = "Gorgon"
                    self.EnemyName.setText(this.EnemyName)
                    this.HPEnemy = 60
                    this.MaxHPEnemy = 60
                    self.EnemyHealth.setText(str(this.HPEnemy)+'/'+str(this.MaxHPEnemy))
                    this.Enum = 15
                elif(Roll > 59 and Roll <= 74):
                    self.textBrowser.append('You encountered a Hydra')
                    this.EnemyName = "Hydra"
                    self.EnemyName.setText(this.EnemyName)
                    this.HPEnemy = 60
                    this.MaxHPEnemy = 60
                    self.EnemyHealth.setText(str(this.HPEnemy)+'/'+str(this.MaxHPEnemy))
                    this.Enum = 16
                elif(Roll > 74 and Roll <= 89):
                    self.textBrowser.append('You encountered a Greater Demon')
                    this.EnemyName = "G. Demon"
                    self.EnemyName.setText(this.EnemyName)
                    this.HPEnemy = 50
                    this.MaxHPEnemy = 50
                    self.EnemyHealth.setText(str(this.HPEnemy)+'/'+str(this.MaxHPEnemy))
                    this.Enum = 17
                else:  
                    self.textBrowser.append('You encountered a Kraken')
                    this.EnemyName = "Kraken"
                    self.EnemyName.setText(this.EnemyName)
                    this.HPEnemy = 40
                    this.MaxHPEnemy = 40
                    self.EnemyHealth.setText(str(this.HPEnemy)+'/'+str(this.MaxHPEnemy))
                    this.Enum = 18
        else:
            if(Roll <= 9):
                self.textBrowser.append('You encountered a Slime')
                this.EnemyName = "Slime"
                self.EnemyName.setText(this.EnemyName)
                this.HPEnemy = 10
                this.MaxHPEnemy = 10
                self.EnemyHealth.setText(str(this.HPEnemy)+'/'+str(this.MaxHPEnemy))
                this.Enum = 1
            elif(Roll > 9 and Roll <= 19):
                self.textBrowser.append('You encountered a Golem')
                this.EnemyName = "Golem"
                self.EnemyName.setText(this.EnemyName)
                this.HPEnemy = 20
                this.MaxHPEnemy = 20
                self.EnemyHealth.setText(str(this.HPEnemy)+'/'+str(this.MaxHPEnemy))
                this.Enum = 2
            elif(Roll > 19 and Roll <= 29):
                self.textBrowser.append('You encountered a Vulture')
                this.EnemyName = "Vulture"
                self.EnemyName.setText(this.EnemyName)
                this.HPEnemy = 12
                this.MaxHPEnemy = 12
                self.EnemyHealth.setText(str(this.HPEnemy)+'/'+str(this.MaxHPEnemy))
                this.Enum = 3
            elif(Roll > 29 and Roll <= 34):
                self.textBrowser.append('You encountered a Kobold')
                this.EnemyName = "Kobold"
                self.EnemyName.setText(this.EnemyName)
                this.HPEnemy = 10
                this.MaxHPEnemy = 10
                self.EnemyHealth.setText(str(this.HPEnemy)+'/'+str(this.MaxHPEnemy))
                this.Enum = 4
            elif(Roll > 34 and Roll <= 39):
                self.textBrowser.append('You encountered a Goblin')
                this.EnemyName = "Goblin"
                self.EnemyName.setText(this.EnemyName)
                this.HPEnemy = 10
                this.MaxHPEnemy = 10
                self.EnemyHealth.setText(str(this.HPEnemy)+'/'+str(this.MaxHPEnemy))
                this.Enum = 5
            elif(Roll > 39 and Roll <= 49):
                self.textBrowser.append('You encountered a Troll')
                this.EnemyName = "Troll"
                self.EnemyName.setText(this.EnemyName)
                this.HPEnemy = 20
                this.MaxHPEnemy = 20
                self.EnemyHealth.setText(str(this.HPEnemy)+'/'+str(this.MaxHPEnemy))
                this.Enum = 6
            elif(Roll > 49 and Roll <= 59):
                self.textBrowser.append('You encountered a Vampire')
                this.EnemyName = "Vampire"
                self.EnemyName.setText(this.EnemyName)
                this.HPEnemy = 20
                this.MaxHPEnemy = 20
                self.EnemyHealth.setText(str(this.HPEnemy)+'/'+str(this.MaxHPEnemy))
                this.Enum = 7
            elif(Roll > 59 and Roll <= 69):
                self.textBrowser.append('You encountered a Skeleton')
                this.EnemyName = "Skeleton"
                self.EnemyName.setText(this.EnemyName)
                this.HPEnemy = 20
                this.MaxHPEnemy = 20
                self.EnemyHealth.setText(str(this.HPEnemy)+'/'+str(this.MaxHPEnemy))
                this.Enum = 8  
            elif(Roll > 69 and Roll <= 79):
                self.textBrowser.append('You encountered a Spooder')
                this.EnemyName = "Spooder"
                self.EnemyName.setText(this.EnemyName)
                this.HPEnemy = 15
                this.MaxHPEnemy = 15
                self.EnemyHealth.setText(str(this.HPEnemy)+'/'+str(this.MaxHPEnemy))
                this.Enum = 9
            elif(Roll > 79 and Roll <= 89):
                self.textBrowser.append('You encountered a Lesser Demon')
                this.EnemyName = "L. Demon"
                self.EnemyName.setText(this.EnemyName)
                this.HPEnemy = 30
                this.MaxHPEnemy = 30
                self.EnemyHealth.setText(str(this.HPEnemy)+'/'+str(this.MaxHPEnemy))
                this.Enum = 10
            else:
                self.textBrowser.append('You encountered a Siren')
                this.EnemyName = "Siren"
                self.EnemyName.setText(this.EnemyName)
                this.HPEnemy = 20
                this.MaxHPEnemy = 20
                self.EnemyHealth.setText(str(this.HPEnemy)+'/'+str(this.MaxHPEnemy))
                this.Enum = 11
    def dead(this,self):
        self.textBrowser.clear()
        self.textBrowser.append("Aw he/she dead\n")
        self.textBrowser.append("You defeated "+str(this.Defeated)+ " monsters")
        question = QMessageBox.question(self.GameWindow, "Exit Game?", "Do you want to continue?")
        
        if question == QMessageBox.Yes:
            self.textBrowser.clear()
            this.HPPlayer = 100
            this.Defeated = 0
            self.Health.setText(str(this.HPPlayer)+"/"+str(this.MaxHPPlayer))
            GameProper.EnemyRoll(this,self)
        else:
            self.GameWindow.close()
    def DiceRoll(this,self):
        HoldEatk = 0 #holds enemy attack
        HoldHatk = 0 #holds hero attack 
        self.textBrowser.clear()
        if(this.HPEnemy <= 0 or this.HPPlayer <= 0):
            if(this.HPPlayer<=0):
                GameProper.dead(this,self)
            else:
                this.Defeated += 1
                print(this.Defeated)
                if(this.Enum<=11):
                    heal = random.randint(5,10)
                    this.HPPlayer += heal
                    self.Health.setText(str(this.HPPlayer)+"/"+str(this.MaxHPPlayer))
                else:
                    heal = random.randint(10,20)
                    this.HPPlayer += heal
                    self.Health.setText(str(this.HPPlayer)+"/"+str(this.MaxHPPlayer))
                GameProper.EnemyRoll(this,self)
        else:
            if self.Actions.checkedButton().text() == "Attack":
                HoldHatk = random.randint(MinAtk[0],MaxAtk[0])
                HoldEatk = random.randint(MinAtk[Enum],MaxAtk[Enum])
                
                self.textBrowser.clear()
                self.textBrowser.append("You attacked the monster for "+ str(HoldHatk) + " damage")
                self.textBrowser.append(this.EnemyName + " Attacked for "+ str(HoldEatk) + " damage")
                self.textBrowser.append("You've taken " + str(HoldEatk) + " damage")
                this.HPPlayer -= HoldEatk
                this.HPEnemy -= HoldHatk
                
                self.Health.setText(str(this.HPPlayer)+"/"+str(this.MaxHPPlayer))
                self.EnemyHealth.setText(str(this.HPEnemy)+"/"+str(this.MaxHPEnemy))

            elif self.Actions.checkedButton().text() == "Block":
                Block = random.randint(MinAtk[Enum],MaxAtk[Enum])
                HoldEatk = random.randint(MinAtk[Enum],MaxAtk[Enum])

                if(Block >= HoldEatk):
                    self.textBrowser.clear()
                    self.textBrowser.append(this.EnemyName + " Attacked for "+ str(HoldEatk) + " damage")
                    self.textBrowser.append("You've successfully blocked " + this.EnemyName + "'s attack!")
                    self.textBrowser.append("You've rebounded " + str(Block-HoldEatk) + " damage")

                    this.HPEnemy -= (Block-HoldEatk)
                    self.EnemyHealth.setText(str(this.HPEnemy)+"/"+str(this.MaxHPEnemy))
                else:
                    self.textBrowser.clear()
                    self.textBrowser.append(this.EnemyName + " Attacked for "+ str(HoldEatk) + " damage")
                    self.textBrowser.append("You've blocked " + str(Block) + " damage")
                    self.textBrowser.append("You took " + str(abs(Block-HoldEatk)) + " damage")

                    this.HPPlayer -= abs(HoldEatk-Block)
                    self.Health.setText(str(this.HPPlayer)+"/"+str(this.MaxHPPlayer))

            elif self.Actions.checkedButton().text() == "Flee":
                HoldEatk = random.randint(MinAtk[Enum],MaxAtk[Enum])
                Flee = random.randint(0,100)

                if(Flee > 50):
                    self.textBrowser.clear()
                    self.textBrowser.append("You've successfully Fled...")
                    GameProper.EnemyRoll(this,self)
                else:
                    self.textBrowser.clear()
                    self.textBrowser.append("You failed to flee")
                    self.textBrowser.append("You took " + str(HoldEatk) + " damage")
                    this.HPPlayer -= HoldEatk
                    self.Health.setText(str(this.HPPlayer)+"/"+str(this.MaxHPPlayer))
    def SaveAndExitGame(this,self):
        '''
        saves the game before exiting
        values of the document:
        0 Player Name
        1 Hp of the Player
        2 HP of the enemy
        3 maximum enemy health
        4 enemy name
        5  enemy number
        6 the number of enemies defeated
        '''
        question = QMessageBox.question(self.GameWindow, "Exit Game?", "Are you sure you want to exit the game?")
        if question == QMessageBox.Yes:
            save = open('save.txt',"a")
            save.write("\n"+str(this.HPPlayer) + "\n" + str(this.HPEnemy) + "\n" + str(this.MaxHPEnemy) + "\n" + str(this.EnemyName) + "\n" + str(this.Enum) + "\n" + str(this.Defeated))
            save.close()
            exitbutton = QMessageBox.information(self.GameWindow, "saved", "Game has been saved")
            if exitbutton:
                self.GameWindow.close()
    
class Ui_GameWindow(object):
    def setupUi(self, GameWindow):
        self.GameWindow = GameWindow
        Gamering = GameProper(1,0,100,1,"Brown","Hero",100,0)
        GameWindow.setObjectName("GameWindow")
        GameWindow.setEnabled(True)
        GameWindow.resize(305, 452)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GameWindow.sizePolicy().hasHeightForWidth())
        GameWindow.setSizePolicy(sizePolicy)
        GameWindow.setMinimumSize(QtCore.QSize(305, 452))
        GameWindow.setMaximumSize(QtCore.QSize(305, 452))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/zjbar/Documents/NetBeansProjects/FinalProj/Image/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        GameWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(GameWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 281, 192))
        self.textBrowser.setObjectName("textBrowser")
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setReadOnly(True)

        self.PlayerName = QtWidgets.QLabel(self.centralwidget)
        self.PlayerName.setGeometry(QtCore.QRect(10, 210, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)

        #Enemy Name, Player health, Enemy Health
        self.EnemyName = QtWidgets.QLabel(self.centralwidget)
        self.EnemyName.setGeometry(QtCore.QRect(170, 210, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        self.EnemyName.setFont(font)
        self.EnemyName.setObjectName("EnemyName")
        self.EnemyName.setAlignment(Qt.AlignCenter)
        self.Health = QtWidgets.QLabel(self.centralwidget)
        self.Health.setGeometry(QtCore.QRect(10, 250, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.Health.setFont(font)
        self.Health.setObjectName("Health")
        self.Health.setAlignment(Qt.AlignCenter)
        self.EnemyHealth = QtWidgets.QLabel(self.centralwidget)
        self.EnemyHealth.setGeometry(QtCore.QRect(170, 250, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.EnemyHealth.setFont(font)
        self.EnemyHealth.setObjectName("EnemyHealth")
        self.EnemyHealth.setAlignment(Qt.AlignCenter)

        #PlayerName
        self.PlayerName.setFont(font)
        self.PlayerName.setObjectName("PlayerName")
        self.PlayerName.setAlignment(Qt.AlignCenter)
        Gamering.PlayerName = self.PlayerName.text()
        Gamering.EnemyRoll(self)
        
            
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(130, 230, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 270, 311, 16))
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.Attack = QtWidgets.QRadioButton(self.centralwidget)
        self.Attack.setGeometry(QtCore.QRect(20, 300, 95, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)

        '''
        Actions
        '''
        self.Attack.setFont(font)
        self.Attack.setObjectName("Attack")
        self.Attack.setChecked(True)
        self.Actions = QtWidgets.QButtonGroup(GameWindow)
        self.Actions.setObjectName("Actions")
        self.Actions.addButton(self.Attack)
        self.Block = QtWidgets.QRadioButton(self.centralwidget)
        self.Block.setGeometry(QtCore.QRect(20, 320, 95, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.Block.setFont(font)
        self.Block.setObjectName("Block")
        self.Actions.addButton(self.Block)
        self.Flee = QtWidgets.QRadioButton(self.centralwidget)
        self.Flee.setGeometry(QtCore.QRect(20, 340, 95, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.Flee.setFont(font)
        self.Flee.setObjectName("Flee")
        self.Actions.addButton(self.Flee)


        '''
        Dice Roll
        '''
        self.Roll = QtWidgets.QPushButton(self.centralwidget)
        self.Roll.setGeometry(QtCore.QRect(140, 300, 147, 61))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.Roll.setFont(font)
        self.Roll.setObjectName("Roll")
        self.Roll.clicked.connect(lambda :Gamering.DiceRoll(self))

        '''
        Save and Exit
        '''
        self.SaveExit = QtWidgets.QPushButton(self.centralwidget)
        self.SaveExit.setGeometry(QtCore.QRect(80, 380, 147, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SaveExit.setFont(font)
        self.SaveExit.setObjectName("SaveExit")
        self.SaveExit.clicked.connect(lambda:Gamering.SaveAndExitGame(self))

        GameWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(GameWindow)
        self.statusbar.setObjectName("statusbar")
        GameWindow.setStatusBar(self.statusbar)
        self.retranslateUi(GameWindow)
        QtCore.QMetaObject.connectSlotsByName(GameWindow)

    def retranslateUi(self, GameWindow):
        _translate = QtCore.QCoreApplication.translate
        GameWindow.setWindowTitle(_translate("GameWindow", "Endless Text Dungeon"))
        self.Health.setText(_translate("GameWindow", "100/100"))
        self.label_5.setText(_translate("GameWindow", "VS"))
        self.Attack.setText(_translate("GameWindow", "Attack"))
        self.Block.setText(_translate("GameWindow", "Block"))
        self.Flee.setText(_translate("GameWindow", "Flee"))
        self.Roll.setText(_translate("GameWindow", "Roll"))
        self.SaveExit.setText(_translate("GameWindow", "Save and Exit"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GameWindow = QtWidgets.QMainWindow()
    ui = Ui_GameWindow()
    ui.setupUi(GameWindow)
    GameWindow.show()
    sys.exit(app.exec_())

