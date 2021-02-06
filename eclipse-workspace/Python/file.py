'''
Created on Mar 28, 2019

@author: sihuh
'''
import sys
import os
from PySide2 import QtUiTools, QtGui
from PySide2.QtWidgets import QApplication, QMainWindow



class MainView(QMainWindow):    

    #__slots__ = ()
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        global UI_set
        UI_set = QtUiTools.QUiLoader().load(resource_path("./file.ui"))
 
 
 
        UI_set.BTN.clicked.connect(self.fileread)
        
        self.setCentralWidget(UI_set)
        self.setWindowTitle("file read and write")
        #self.setWindowIcon(QtGui.QPixmap(resource_path("./images/bbok.png")))
        self.resize(775,537) 
        self.show() 
    
    def fileread(self):
        
        text = UI_set.lineEdit.text()
        f = open('file.txt','a')
        f.write(text + '\n')
        f.close()
        
        f = open('file.txt','r')
        data = f.read()
        UI_set.result.setText(data)
        f.close







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
