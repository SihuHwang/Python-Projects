'''
Created on Mar 2, 2019

@author: sihuh
'''
import sys

import os

from PySide2 import QtUiTools, QtGui

from PySide2.QtWidgets import QApplication, QMainWindow
from _ast import If                 , Try

 

class MainView(QMainWindow):    

    #__slots__ = ()

    def __init__(self):

        super().__init__()

        self.setupUI()

    def setupUI(self):
        global UI_set
        UI_set = QtUiTools.QUiLoader().load(resource_path("./Vending.ui"))
        
        UI_set.BTN_Cola.clicked.connect(self.cola)
        UI_set.BTN_Sprite.clicked.connect(self.Sprite)
        UI_set.BTN_Dr.clicked.connect(self.Dr)
        
        
             
        
 
        self.setCentralWidget(UI_set)

        self.setWindowTitle("Vending Machine")

        #self.setWindowIcon(QtGui.QPixmap(resource_path("./images/bbok.png")))

        self.resize(917,846) 
        self.show()
        
    def cola(self):
        #UI_set.Soda.setText('You pressed the Cola button')
    
        Cola_Price = float(UI_set.Cola_Price.toPlainText())
        try:
            Money = float(UI_set.Money.toPlainText())
        except:
            Money = 0.0
            print('please insert a number')
        
        print(Cola_Price)
        print(Money)
        
        if(Money >= Cola_Price):
          
            
            Cola_Count = int(UI_set.Cola_Count.text())
            
            if(Cola_Count > 0):
                UI_set.Cola_Count.setText(str(Cola_Count-1))
                UI_set.Soda.setText('Here is your %d Soda' % 1)
               
                leftover = Money - Cola_Price
                
                if(leftover >= Cola_Price):
                     UI_set.Money.setText(str(leftover))
                     UI_set.Change.setText('')
                else:
                    UI_set.Change.setText(str(leftover))
                    UI_set.Money.setText('0')
            
            else:
                     UI_set.Soda.setText('All out of Cola')
                    
           
            
        else:
            UI_set.Soda.setText('You do not have enough money')    
    
    def Sprite(self):
        Sprite_Price = float(UI_set.Sprite_Price.toPlainText())
        try:
            Money = float(UI_set.Money.toPlainText())
        except:
            Money = 0.0
            print('please insert a number')
        
        print(Sprite_Price)
        
        if(Money >= Sprite_Price):
          
            
            Sprite_Count = int(UI_set.Sprite_Count.toPlainText())
            
            if(Sprite_Count > 0):
                UI_set.Sprite_Count.setText(str(Sprite_Count-1))
                UI_set.Soda.setText('Here is your %d Soda' % 1)
               
                leftover = Money - Sprite_Price
                
                if(leftover >= Sprite_Price):
                     UI_set.Money.setText(str(leftover))
                     UI_set.Change.setText('')
                else:
                    UI_set.Change.setText(str(leftover))
                    UI_set.Money.setText('0')
            
            else:
                     UI_set.Soda.setText('All out of Sprite')
                    
           
            
        else:
            UI_set.Soda.setText('You do not have enough money')    
    
    def Dr(self):
        Dr_Price = float(UI_set.Dr_Price.toPlainText())
        try:
            Money = float(UI_set.Money.toPlainText())
        except:
            Money = 0.0
            print('please insert a number')
        print(Dr_Price)
        
        if(Money >= Dr_Price):
          
            
            Dr_Count = int(UI_set.Dr_Count.toPlainText())
            
            if(Dr_Count > 0):
                UI_set.Dr_Count.setText(str(Dr_Count-1))
                UI_set.Soda.setText('Here is your %d Soda' % 1)
               
                leftover = Money - Dr_Price
                
                if(leftover >= Dr_Price):
                     UI_set.Money.setText(str(leftover))
                     UI_set.Change.setText('')
                else:
                    UI_set.Change.setText(str(leftover))
                    UI_set.Money.setText('0')
            
            else:
                     UI_set.Soda.setText('All out of Dr Pepper')
                    
           
            
        else:
            UI_set.Soda.setText('You do not have enough money')    
                




#파일 경로
        
#pyinstaller로 원파일로 압축할때 경로 필요함

def resource_path(relative_path):

    if hasattr(sys, '_MEIPASS'):

        return os.path.join(sys._MEIPASS, relative_path)

    return os.path.join(os.path.abspath("."), relative_path)

 

if __name__ == '__main__':  

    app = QApplication(sys.argv)

    main = MainView()

    #main.show()

    sys.exit(app.exec_())   