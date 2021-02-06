'''
Created on Nov 26, 2019

@author: sihuh
'''
import sys
import os
from PySide2 import QtUiTools, QtGui
from PySide2.QtWidgets import QApplication, QMainWindow,QMessageBox



class MainView(QMainWindow):    

    #__slots__ = ()
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.fileopen()
    def setupUI(self):
        global UI_set, UI_setting
        UI_set = QtUiTools.QUiLoader().load(resource_path("./project.ui"))

        UI_setting = QtUiTools.QUiLoader().load(resource_path("./setting.ui"))
        UI_setting.setWindowTitle('Count and Price')
        UI_setting.resize(344,335)

        UI_set.BTN_Setting.clicked.connect(self.setting)
        UI_setting.BTN_Load.clicked.connect(Price_Count)
        UI_setting.BTN_Save.clicked.connect(Save_Price_Count)

        UI_set.BTN_Cola.clicked.connect(self.Cola)
        UI_set.BTN_Sprite.clicked.connect(self.Sprite)
        UI_set.BTN_Dr.clicked.connect(self.Dr)
        UI_set.BTN_Monster.clicked.connect(self.Monster)
        UI_set.Box_Money.valueChanged.connect(Check)
        
        self.setCentralWidget(UI_set)
        self.setWindowTitle("project")
        #self.setWindowIcon(QtGui.QPixmap(resource_path("./images/bbok.png")))
        self.resize(780,443)
        self.show()



    
    def fileopen(self):
        global Vending_Price 
        Vending_Price = {'Cola_Price':10, 'Cola_Count':5,
                         'Sprite_Price':8,'Sprite_Count':5, 
                         'Pepper_Price':6, 'Pepper_Count':5, 
                         'Monster_Price':4, 'Monster_Count':5}
        
        try: 
            f = open('Vending.txt','r')
            data = f.readline()
            f.close
            Vending_Price = eval(data)
            
        except:
            f = open('Vending.txt','w')
            f.write(str(Vending_Price))
            f.close
            
        Check()


    def setting(self):
        UI_setting.show()
        UI_setting.activateWindow()
        

    def Cola(self):
        result = messageBox('Cola', 'Are you sure? ', 'You are buying 1 COLA', 'b',Vending_Price.get('Cola_Count'))

        if result == QMessageBox.Yes:

            Vending_Price['Cola_Count'] = Vending_Price.get('Cola_Count') - 1
            money = UI_set.Box_Money.value() - Vending_Price.get('Cola_Price')
            UI_set.Box_Money.setValue(money)
            Check()
        elif result == QMessageBox.No:
            pass
        
        

        
        
    def Sprite(self):
        result = messageBox('Sprite', 'Are you sure? ', 'You are buying 1 SPRITE', 'b', Vending_Price.get('Sprite_Count'))

        if result == QMessageBox.Yes:
            Vending_Price['Sprite_Count'] = Vending_Price.get('Sprite_Count') - 1
            money = UI_set.Box_Money.value() - Vending_Price.get('Sprite_Price')
            UI_set.Box_Money.setValue(money)
            Check()
        elif result == QMessageBox.No:
            pass
        
    def Dr (self):
        result = messageBox('Dr.Pepper', 'Are you sure? ', 'You are buying 1 DR.PEPPER', 'b', Vending_Price.get('Pepper_Count'))

        if result == QMessageBox.Yes:

            Vending_Price['Pepper_Count'] = Vending_Price.get('Pepper_Count') - 1
            money = UI_set.Box_Money.value() - Vending_Price.get('Pepper_Price')
            UI_set.Box_Money.setValue(money)
            Check()
        elif result == QMessageBox.No:
            pass
            
    def Monster (self):
        result = messageBox('Monster', 'Are you sure? ', 'You are buying 1 MONSTER', 'b', Vending_Price.get('Monster_Count'))

        if result == QMessageBox.Yes:
            Vending_Price['Monster_Count'] = Vending_Price.get('Monster_Count') - 1
            money = UI_set.Box_Money.value() - Vending_Price.get('Monster_Price')
            UI_set.Box_Money.setValue(money)
            Check()
        elif result == QMessageBox.No:
            pass

        # if result == QMessageBox.Ok:
        #     Vending_Price['Monster_Count'] = Vending_Price.get('Monster_Count') - 1
        #     money = UI_set.Box_Money.value() - Vending_Price.get('Monster_Price')
        #     UI_set.Box_Money.setValue(money)
        #     Check()

def Check():
    global Vending_Price, UI_set

    # print('a')
    money = UI_set.Box_Money.value()
    Cola_Price = Vending_Price.get('Cola_Price', 10)
    Cola_Count = Vending_Price.get('Cola_Count', 5)
    Sprite_Price = Vending_Price.get('Sprite_Price', 8)
    Sprite_Count = Vending_Price.get('Sprite_Count', 5)
    Dr_Price = Vending_Price.get('Pepper_Price', 6)
    Dr_Count = Vending_Price.get('Pepper_Count', 5)
    Monster_Price = Vending_Price.get('Monster_Price', 4)
    Monster_Count = Vending_Price.get('Monster_Count', 5)
    #         print(Dr_Price)
    #         print(Dr_Count)
    #         print(Cola_Count)
    #         print(Cola_Price)
    #         print(Sprite_Count)
    #         print(Sprite_Price)
    #         print(Monster_Count)
    #         print(Monster_Price)

    UI_set.LB_Cola.setText('COLA COUNT:%s' % Vending_Price.get('Cola_Count'))
    UI_set.LB_Sprite.setText('SPRITE COUNT:%s' % Vending_Price.get('Sprite_Count'))
    UI_set.LB_Dr.setText('DR.PEPPER COUNT:%s' % Vending_Price.get('Pepper_Count'))
    UI_set.LB_Monster.setText('MONSTER COUNT:%s' % Vending_Price.get('Monster_Count'))

    if money >= Cola_Price and Cola_Count > 0:
        UI_set.BTN_Cola.setStyleSheet('background-color:#FDFEFE')
        UI_set.BTN_Cola.setEnabled(True)
    else:
        UI_set.BTN_Cola.setStyleSheet('background-color:#ff0000')
        UI_set.BTN_Cola.setEnabled(False)

    if money >= Sprite_Price and Sprite_Count > 0:
        UI_set.BTN_Sprite.setStyleSheet('background-color:#FDFEFE')
        UI_set.BTN_Sprite.setEnabled(True)
    else:
        UI_set.BTN_Sprite.setStyleSheet('background-color:#ff0000')
        UI_set.BTN_Sprite.setEnabled(False)

    if money >= Dr_Price and Dr_Count > 0:
        UI_set.BTN_Dr.setStyleSheet('background-color:#FDFEFE')
        UI_set.BTN_Dr.setEnabled(True)
    else:
        UI_set.BTN_Dr.setStyleSheet('background-color:#ff0000')
        UI_set.BTN_Dr.setEnabled(False)

    if money >= Monster_Price and Monster_Count > 0:
        UI_set.BTN_Monster.setStyleSheet('background-color:#FDFEFE')
        UI_set.BTN_Monster.setEnabled(True)
    else:
        UI_set.BTN_Monster.setStyleSheet('background-color:#ff0000')
        UI_set.BTN_Monster.setEnabled(False)

    f = open('Vending.txt', 'w')
    f.write(str(Vending_Price))
    f.close()

def Price_Count():


        f = open('Vending.txt', 'r')
        data = f.readline()
        f.close
        Vending_Price = eval(data)
        # print(Vending_Price)

        UI_setting.SB_CP.setValue(Vending_Price.get('Cola_Price'))
        UI_setting.SB_SP.setValue(Vending_Price.get('Sprite_Price'))
        UI_setting.SB_DP.setValue(Vending_Price.get('Pepper_Price'))
        UI_setting.SB_MP.setValue(Vending_Price.get('Monster_Price'))
        UI_setting.SB_CC.setValue(Vending_Price.get('Cola_Count'))
        UI_setting.SB_SC.setValue(Vending_Price.get('Sprite_Count'))
        UI_setting.SB_DC.setValue(Vending_Price.get('Pepper_Count'))
        UI_setting.SB_MC.setValue(Vending_Price.get('Monster_Count'))

def Save_Price_Count():
    global Vending_Price

    CP = UI_setting.SB_CP.value()
    CC = UI_setting.SB_CC.value()
    SP = UI_setting.SB_SP.value()
    SC = UI_setting.SB_SC.value()
    DP = UI_setting.SB_SP.value()
    DC = UI_setting.SB_DC.value()
    MP = UI_setting.SB_MP.value()
    MC = UI_setting.SB_MC.value()

    Vending_Price = {'Cola_Price': CP, 'Cola_Count':CC,
                     'Sprite_Price': SP, 'Sprite_Count': SC,
                     'Pepper_Price': DP, 'Pepper_Count': DC,
                     'Monster_Price': MP, 'Monster_Count': MC}
    f = open('Vending.txt', 'w')
    f.write(str(Vending_Price))
    f.close

    Check()

    # print(Vending_Price)
def messageBox(windowtitle,title,content,style,count):

    msgbox = QMessageBox()
    msgbox.setWindowTitle(windowtitle)
    msgbox.setWindowIcon(QtGui.QPixmap('alert.png'))
    msgbox.setText(title)
    msgbox.setInformativeText(content)

    if style == 'a':
        msgbox.setStandardButtons(QMessageBox.Yes)
    elif style == 'b':
        msgbox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    elif style == 'c':
        msgbox.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)

    if count == 1:
        msgbox.setStandardButtons(QMessageBox.Ok)


    return msgbox.exec_()




def resource_path(relative_path):

    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

if __name__ == '__main__':  

    app = QApplication(sys.argv)
    main = MainView()
    #main.show()
    sys.exit(app.exec_())   