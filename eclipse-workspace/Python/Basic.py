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
        UI_set = QtUiTools.QUiLoader().load(resource_path("./Vending.ui"))
#         #enable or not 
#         UI_set.pushButton.setEnabled(True)
#         UI_set.pushButton.setEnabled(False)
#         #change background color
#         UI_set.pushbutton.setStyleSheet('background color:#ffffff')
#         
        self.setCentralWidget(UI_set)
        self.setWindowTitle("Vending Machine")
        #self.setWindowIcon(QtGui.QPixmap(resource_path("./images/bbok.png")))
        self.resize(917,846) 
        self.show() 


def resource_path(relative_path):

    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

if __name__ == '__main__':  

    app = QApplication(sys.argv)
    main = MainView()
    #main.show()
    sys.exit(app.exec_())   