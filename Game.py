from os import name
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QDialogButtonBox, QLabel, QMainWindow, QMessageBox, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
import sys
import random

#Declare global variables
global Defeated
global Enum
global HPPlayer
global HPEnemy
global MinAtk
global MaxAtk
global MaxHP
global EnemyName
global PName

#Variables
MinAtk = [7, 1, 4, 3, 1, 1, 5, 3, 1, 1, 5, 4, 10, 13, 15, 10, 7, 15, 15, 7]
MaxAtk = [12, 6, 7, 6, 6, 6, 8, 6, 8, 6, 7, 6, 20, 15, 20, 15, 10, 22, 25, 12]
MaxHP = [100, 0]
Enum = 1 #EnemyNumber
Defeated = 0 #counter for the defeated mobs
HPPlayer = 100
HPEnemy = 1
EnemyName = "Brown"


class GameProper:
    def __init__(this,Enum,Defeated,HPPlayer,HPEnemy,EnemyName,PlayerName):
        this.Enum = Enum
        this.Defeaeted = Defeated
        this.HPPlayer = HPPlayer
        this.HPEnemy = HPEnemy
        this.EnemyName = EnemyName
        this.PlayerName = PlayerName
    def EnemyRoll(this,self):
        from ui import Ui_GameWindow
        Roll = random.randint(1,100)
        self.textBrowser.clear()
        if(this.Defeated >=10 and ((this.Defeated % 30) == 0)):
            if (this.Defeated >= 30 and ((this.Defeated % 30) == 0)):
                self.textBrowser.append("You encountered a Doppelganger")
                this.EnemyName = "Doppelganger"
                self.EnemyName.setText(this.EnemyName)
                this.HPEnemy = 100
                self.EnemyHealth.setText(str(this.HPEnemy)+'/100')
                this.Enum = 19

            else:
                if(Roll <= 15):
                    self.textBrowser.append('You encountered a Spider Broodmother')
                    this.EnemyName = "Spooder Brod."
                    self.EnemyName.setText(this.EnemyName)
                    this.HPEnemy = 45
                    self.EnemyHealth.setText(str(this.HPEnemy)+'/45')
                    this.Enum = 12

                elif(Roll > 15 and Roll <= 29):
                    self.textBrowser.append('You encountered a Vampire Lord')
                    this.EnemyName = "Vampire Lord"
                    self.EnemyName.setText(this.EnemyName)
                    this.HPEnemy = 60
                    self.EnemyHealth.setText(str(this.HPEnemy)+'/60')
                    this.Enum = 13
                elif(Roll > 29 and Roll <= 44):
                    self.textBrowser.append('You encountered a T. Rex')
                    this.EnemyName = "T. Rex"
                    self.EnemyName.setText(this.EnemyName)
                    this.HPEnemy = 45
                    self.EnemyHealth.setText(str(this.HPEnemy)+'/45')
                    this.Enum = 14
                elif(Roll > 44 and Roll <= 59):
                    self.textBrowser.append('You encountered a Gorgon')
                    this.EnemyName = "Gorgon"
                    self.EnemyName.setText(this.EnemyName)
                    this.HPEnemy = 60
                    self.EnemyHealth.setText(str(this.HPEnemy)+'/60')
                    this.Enum = 15
                elif(Roll > 59 and Roll <= 74):
                    self.textBrowser.append('You encountered a Hydra')
                    this.EnemyName = "Hydra"
                    self.EnemyName.setText(this.EnemyName)
                    this.HPEnemy = 60
                    self.EnemyHealth.setText(str(this.HPEnemy)+'/60')
                    this.Enum = 16
                elif(Roll > 74 and Roll <= 89):
                    self.textBrowser.append('You encountered a Greater Demon')
                    this.EnemyName = "G. Demon"
                    self.EnemyName.setText(this.EnemyName)
                    this.HPEnemy = 50
                    self.EnemyHealth.setText(str(this.HPEnemy)+'/50')
                    this.Enum = 17
                else:  
                    self.textBrowser.append('You encountered a Kraken')
                    this.EnemyName = "Kraken"
                    self.EnemyName.setText(this.EnemyName)
                    this.HPEnemy = 40
                    self.EnemyHealth.setText(str(this.HPEnemy)+'/40')
                    this.Enum = 18
        else:
            if(Roll <= 9):
                self.textBrowser.append('You encountered a Slime')
                this.EnemyName = "Slime"
                self.EnemyName.setText(this.EnemyName)
                this.HPEnemy = 10
                self.EnemyHealth.setText(str(this.HPEnemy)+'/10')
                this.Enum = 1
            elif(Roll > 9 and Roll <= 19):
                self.textBrowser.append('You encountered a Golem')
                this.EnemyName = "Golem"
                self.EnemyName.setText(this.EnemyName)
                this.HPEnemy = 20
                self.EnemyHealth.setText(str(this.HPEnemy)+'/20')
                this.Enum = 2
            elif(Roll > 19 and Roll <= 29):
                self.textBrowser.append('You encountered a Vulture')
                this.EnemyName = "Vulture"
                self.EnemyName.setText(this.EnemyName)
                this.HPEnemy = 12
                self.EnemyHealth.setText(str(this.HPEnemy)+'/12')
                this.Enum = 3
            elif(Roll > 29 and Roll <= 34):
                self.textBrowser.append('You encountered a Kobold')
                this.EnemyName = "Kobold"
                self.EnemyName.setText(this.EnemyName)
                this.HPEnemy = 10
                self.EnemyHealth.setText(str(this.HPEnemy)+'/10')
                this.Enum = 4
            elif(Roll > 34 and Roll <= 39):
                self.textBrowser.append('You encountered a Goblin')
                this.EnemyName = "Goblin"
                self.EnemyName.setText(this.EnemyName)
                this.HPEnemy = 10
                self.EnemyHealth.setText(str(this.HPEnemy)+'/10')
                this.Enum = 5
            elif(Roll > 39 and Roll <= 49):
                self.textBrowser.append('You encountered a Troll')
                this.EnemyName = "Troll"
                self.EnemyName.setText(this.EnemyName)
                this.HPEnemy = 20
                self.EnemyHealth.setText(str(this.HPEnemy)+'/20')
                this.Enum = 6
            elif(Roll > 49 and Roll <= 59):
                self.textBrowser.append('You encountered a Vampire')
                this.EnemyName = "Vampire"
                self.EnemyName.setText(this.EnemyName)
                this.HPEnemy = 20
                self.EnemyHealth.setText(str(this.HPEnemy)+'/20')
                this.Enum = 7
            elif(Roll > 59 and Roll <= 69):
                self.textBrowser.append('You encountered a Skeleton')
                this.EnemyName = "Skeleton"
                self.EnemyName.setText(this.EnemyName)
                this.HPEnemy = 20
                self.EnemyHealth.setText(str(this.HPEnemy)+'/20')
                this.Enum = 8  
            elif(Roll > 69 and Roll <= 79):
                self.textBrowser.append('You encountered a Spooder')
                this.EnemyName = "Spooder"
                self.EnemyName.setText(this.EnemyName)
                this.HPEnemy = 15
                self.EnemyHealth.setText(str(this.HPEnemy)+'/15')
                this.Enum = 9
            elif(Roll > 79 and Roll <= 89):
                self.textBrowser.append('You encountered a Lesser Demon')
                this.EnemyName = "L. Demon"
                self.EnemyName.setText(this.EnemyName)
                this.HPEnemy = 30
                self.EnemyHealth.setText(str(this.HPEnemy)+'/30')
                this.Enum = 10
            else:
                self.textBrowser.append('You encountered a Siren')
                this.EnemyName = "Siren"
                self.EnemyName.setText(this.EnemyName)
                this.HPEnemy = 20
                self.EnemyHealth.setText(str(this.HPEnemy)+'/20')
                this.Enum = 11
    def dead(self,this):
        from ui import Ui_GameWindow
        self.textBrowser.clear()
        self.textBrowser.append("Aw he dead\n")
        self.textBrowser.append("You defeated "+str(this.Defeated)+ " monsters")
        question = QMessageBox.question(self, "Exit Game?", "Do you want to continue?")
        
        if question == QMessageBox.Yes:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_GameWindow()
            self.ui.setupUi(self.window)
            self.window.show()
        else:
            self.close()
    def DiceRoll(self,this):
        HoldEatk = 0 #holds enemy attack
        HoldHatk = 0 #holds hero attack 
        HoldHHP = 0 #hold hero HP
        HoldEHP = 0 #hold enemy HP
        HoldDef = 0 #hold Defeated number
        self.textBrowser.clear()
        if(this.HPEnemy <= 0 or this.HPPlayer <= 0):
            if(this.HPPlayer<=0):
                GameProper.dead()
            elif(this.Enum == 0):
                GameProper.EnemyRoll()
            else:
                Defeated = HoldDef + 1
                if(Enum<=11):
                    heal = random.randint(10,15)
                    HoldHHP = this.HPPlayer + heal
                    self.Health.setText(HoldHHP+"/"+str(MaxHP[0]))
                else:
                    heal = random.randint(25,50)
                    HoldHHP = this.HPPlayer + heal
                    self.Health.setText(HoldHHP+"/"+str(MaxHP[0]))
                self.EnemyRoll()
        else:
            if self.Actions.checkedButton().text() == "Attack":
                HoldHatk = random.randint(MinAtk[0],MaxAtk[0])
                HoldEatk = random.randint(MinAtk[Enum],MaxAtk[Enum])
                
                self.textBrowser.clear()
                self.textBrowser.append("You attacked the monster for "+ str(HoldHatk) + " damage")
                self.textBrowser.append(EnemyName + " Attacked for "+ str(HoldEatk) + " damage")
                self.textBrowser.append("You've taken " + str(HoldEatk) + " damage")
                HoldHHP = this.HPPlayer - HoldEatk
                HoldEHP = this.HPEnemy - HoldHatk
                
                self.Health.setText(str(HoldHHP)+"/"+str(MaxHP[0]))
                self.EnemyHealth.setText(str(HoldEHP)+"/"+str(MaxHP[1]))

            elif self.Actions.checkedButton().text() == "Block":
                Block = random.randint(MinAtk[Enum],MaxAtk[Enum])
                HoldEatk = random.randint(MinAtk[Enum],MaxAtk[Enum])

                if(Block >= HoldEatk):
                    self.textBrowser.clear()
                    self.textBrowser.append(str(EnemyName) + " Attacked for "+ str(HoldEatk) + " damage")
                    self.textBrowser.append("You've successfully blocked " + str(EnemyName) + "'s attack!")
                    self.textBrowser.append("You've rebounded " + str(Block-HoldEatk) + " damage")

                    HoldEHP = (Block-HoldEatk)
                    self.EnemyHealth.setText(str(HoldEHP)+"/"+str(MaxHP[1]))
                else:
                    self.textBrowser.clear()
                    self.textBrowser.append(str(EnemyName) + " Attacked for "+ str(HoldEatk) + " damage")
                    self.textBrowser.append("You've blocked " + str(Block) + " damage")
                    self.textBrowser.append("You took " + str(abs(Block-HoldEatk)) + " damage")

                    HoldHHP = (HoldEatk-Block)
                    self.Health.setText(str(HoldHHP)+"/"+str(MaxHP[0]))

            elif self.Actions.checkedButton().text() == "Flee":
                HoldEatk = random.randint(MinAtk[Enum],MaxAtk[Enum])
                Flee = random.randint(0,100)

                if(Flee > 50):
                    self.textBrowser.clear()
                    self.textBrowser.append("You've successfully Fled...")
                    GameProper.EnemyRoll()
                else:
                    self.textBrowser.clear()
                    self.textBrowser.append("You failed to flee")
                    self.textBrowser.append("You took " + str(this.HoldEatk) + " damage")
                    HoldHHP = HPPlayer - HoldEatk
                    self.Health.setText(str(HoldHHP)+"/"+str(MaxHP[0]))
    def SaveAndExitGame(self, this):
        question = QMessageBox.question(self, "Exit Game?", "Are you sure you want to exit the game?")
        if question == QMessageBox.Yes:
            save = open('save.txt',"w")
            save.write(str(this.HPPlayer) + "\n" + str(this.HPEnemy) + "\n" + str(this.MaxHP) + "\n" + str(this.PName) + "\n" + str(this.EnemyName) + "\n" + str(this.Enum) + "\n" + str(this.Defeated))
            save.close()
            exitbutton = QMessageBox.information(self, "saved", "Game has been saved")
            if exitbutton:
                self.close()
    