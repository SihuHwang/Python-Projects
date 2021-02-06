'''
Created on Jun 11, 2019

@author: sihuh
'''

import sys
import os
from PySide2 import QtUiTools, QtGui , QtCore
from PySide2.QtWidgets import QApplication, QMainWindow , QHeaderView, QTableWidgetItem
from _ast import If                 , Try

class MainView(QMainWindow):                

    #__slots__ = ()
    def __init__(self):
        super().__init__()
        
        self.setupUI()
 
        self.setTable()


    def setupUI(self):
        global UI_set
        UI_set = QtUiTools.QUiLoader().load(resource_path("./widgettest.ui"))
        
        UI_set.pushButton.clicked.connect(self.clickbutton)
 
 
    def setTable(self):
        global UI_set
 
 
        
        self.setCentralWidget(UI_set)
        self.setWindowTitle("widgettest")
        #self.setWindowIcon(QtGui.QPixmap(resource_path("./images/bbok.png")))
        self.resize(917,846) 
        self.show() 
    
        
        #table 세로 갯수

        UI_set.tableWidget.setRowCount(5)        
        UI_set.tableWidget.setColumnCount(2)
        
        UI_set.tableWidget.setHorizontalHeaderLabels(['이름','생일'])
        
        #UI_set.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        #UI_set.tableWidget.setSpan(0,2, 1,4)
        
        UI_set.tableWidget.setColumnWidth(0, 334)
        UI_set.tableWidget.setColumnWidth(1, 334)
        
        for i in range(5): 
                   
            UI_set.tableWidget.setRowHeight(i, 91)
            
            
            UI_set.tableWidget.setItem(i, 0, QTableWidgetItem(""))
            UI_set.tableWidget.setItem(i, 1, QTableWidgetItem(""))
        
              
        font = QtGui.QFont("Comic Sans MS", 10, QtGui.QFont.Normal)
        UI_set.tableWidget.item(0, 0).setBackground(QtGui.QColor("#FFFFFF"))
        UI_set.tableWidget.item(0, 0).setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        UI_set.tableWidget.item(0, 0).setFont(font)
        
        
            
        
    def clickbutton(self):
        print('clicked button')
        #UI_set.tableWidget.item(0, 0).setText("Sihu Hwang")
        
        name = UI_set.lineEdit.text()
        birth = UI_set.lineEdit2.text()
        
        UI_set.tableWidget.item(0, 0).setText(name)
        UI_set.tableWidget.item(0, 1).setText(birth)
        
        
        
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