'''
Created on Apr 4, 2019

@author: sihuh
'''
import sys
import os
import random
from PySide2 import QtUiTools, QtGui
from PySide2.QtWidgets import QApplication, QMainWindow
from _ast import If
from select import select

class MainView(QMainWindow):    

    #__slots__ = ()
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        global UI_set, result_list
        result_list = []
        UI_set = QtUiTools.QUiLoader().load(resource_path("./Game.ui"))
        
        UI_set.BTN_Save.clicked.connect(self.Savefile)
        UI_set.BTN_Start.clicked.connect(self.start)
        self.setCentralWidget(UI_set)
        self.setWindowTitle("Game")
        #self.setWindowIcon(QtGui.QPixmap(resource_path("./images/bbok.png")))
        self.resize(800,600) 
        self.show() 

    def start (self):
        print(' Game Starting')
        try:
            
            Guess = int(UI_set.Guess.text()) 
            randnumber = random.randint(1,100)
            UI_set.Random.setText(str(randnumber))
            gameresult = ''
        
            if Guess < 1 or Guess > 100:
                UI_set.Result.setText('pick a number 1-100 please')
                UI_set.Guess.setFocus()           
                     
            else: 
                UI_set.Random.setText(str(randnumber))
                Selector = ''
                
                if UI_set.BTN_Up.isChecked():
                    Selector = 'UP'
                elif UI_set.BTN_Down.isChecked():
                    Selector = 'Down'
                       
                if Selector == '':
                    UI_set.Result.setText('Please select up or down')
                else:
                    
                    if Selector == 'UP':
                        if Guess > randnumber:
                            gameresult = 'WIN'
                        else:
                            gameresult = 'LOSE'
                             
                    elif Selector == 'Down':
                        if Guess < randnumber:
                            gameresult = 'WIN'
                        else:
                            gameresult = 'LOSE'
                            
                resultstr = {'selected number':Guess,'random number':randnumber,'selector ':Selector,'result':gameresult}   
                result_list.append(resultstr)
                UI_set.Result.setText(str(resultstr))
        except:
            UI_set.Result.setText('please enter a number')
            UI_set.Guess.setText('')
            UI_set.Guess.setFocus()
    
    def Savefile(self):
        f = open('game.txt','a')
        
        count = len(result_list)
        for x in range(count):
            f.write(str(result_list[x])+ '\n')
        f.close()
                
            
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