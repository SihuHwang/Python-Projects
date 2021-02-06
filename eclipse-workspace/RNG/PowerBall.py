'''
Created on Mar 14, 2019

@author: sihuh
'''
import sys
import os
import random
from PySide2 import QtUiTools, QtGui
from PySide2.QtWidgets import QApplication, QMainWindow

class MainView(QMainWindow):    

    #__slots__ = ()
    def __init__(self):
        super().__init__()
        self.setupUI()      

    def setupUI(self):
        global UI_set
        UI_set = QtUiTools.QUiLoader().load(resource_path("./PowerBall.ui"))
        
        UI_set.BTN_create.clicked.connect(self.create)
        self.setCentralWidget(UI_set)
        self.setWindowTitle("PowerBall")
        #self.setWindowIcon(QtGui.QPixmap(resource_path("./images/bbok.png")))
        self.resize(840,540) 
        self.show() 
        
    def create(self):
#         print('button pressed')
        
        powernumber = list()
        for i in range(65):
            powernumber.append(i + 1)
#         print(powernumber)

        powerball = list()
        for i in range(25):
            powerball.append(i + 1)
#         print(powerball)
     
        count = len(powernumber)
        for i  in range(count):
            temp1 = powernumber[i]
                       
            r = random.randrange(count)
            temp2=powernumber[r]
            
            powernumber[i] = temp2
            powernumber[r] = temp1
            #print(r)
            
#         print(powernumber)

        
    
        sortvalue = list()
        for i in range(5):
            sortvalue.append(powernumber[i])
        
#         print(sortvalue)
        sortvalue.sort()
#         print(sortvalue)



        UI_set.number_1.setText(str(sortvalue[0]))
        UI_set.number_2.setText(str(sortvalue[1]))    
        UI_set.number_3.setText(str(sortvalue[2]))   
        UI_set.number_4.setText(str(sortvalue[3]))
        UI_set.number_5.setText(str(sortvalue[4]))    
        
        pr = random.randrange(25)
        powerballvalue = powerball[pr]
        UI_set.PowerBall.setText(str(powerballvalue))
        


def resource_path(relative_path):

    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

if __name__ == '__main__':  

    app = QApplication(sys.argv)
    main = MainView()
    #main.show()
    sys.exit(app.exec_())   
    