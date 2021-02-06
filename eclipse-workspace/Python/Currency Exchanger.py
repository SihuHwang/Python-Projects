import sys
import os
from PySide2 import QtUiTools, QtGui
from PySide2.QtWidgets import QApplication, QMainWindow


class MainView(QMainWindow):

    # __slots__ = ()
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        global UI_set
        UI_set = QtUiTools.QUiLoader().load(resource_path("./Currency.ui"))
        #         #enable or not
        #         UI_set.pushButton.setEnabled(True)
        #         UI_set.pushButton.setEnabled(False)
        #         #change background color
        #         UI_set.pushbutton.setStyleSheet('background color:#ffffff')
        UI_set.CB_Input.textActivated.connect(Insert_Currency)
        UI_set.CB_Output.textActivated.connect(Insert_Currency)
        UI_set.BTN_Calculate.clicked.connect(Calculate)
        

        self.setCentralWidget(UI_set)
        self.setWindowTitle("Currency Exchanger")
        # self.setWindowIcon(QtGui.QPixmap(resource_path("./images/bbok.png")))
        self.resize(605, 586)
        self.show()
    # 파일 경로



def Insert_Currency():
    Starting_Currency = UI_set.CB_Input.currentText()
    Ending_Currency = UI_set.CB_Output.currentText()
    if Starting_Currency == 'South Korean Won' and Ending_Currency == 'United States Dollar':
        South_Korean_Dollar()
    elif Starting_Currency == 'United States Dollar' and Ending_Currency == 'South Korean Won':
        United_States_Won()
    elif Starting_Currency == 'Japanese Yen' and Ending_Currency == 'United States Dollar':
        Japanese_Dollar()
    elif Starting_Currency == 'United States Dollar' and Ending_Currency == 'Japanese Yen':
        United_States_Yen()
    elif Starting_Currency == 'Japanese Yen' and Ending_Currency == 'South Korean Won':
        Japanese_Won()
    elif Starting_Currency == 'South Korean Won' and Ending_Currency == ' Japanese Yen':
        South_Korean_Yen()

def South_Korean_Dollar():
    Input_Value = UI_set.TE_Input.toPlainText()
    Calculated_Value = float(Input_Value) * .00084
    UI_set.TE_Output.setText(str(Calculated_Value) + ' United States Won')

def United_States_Won():
    Input_Value = UI_set.TE_Input.toPlainText()
    Calculated_Value = float(Input_Value) * 1194.39
    UI_set.TE_Output.setText(str(Calculated_Value) + ' South Korean Won')
def Japanese_Dollar():
    Input_Value = UI_set.TE_Input.toPlainText()
    Calculated_Value = float(Input_Value) * 0.0094
    UI_set.TE_Output.setText(str(Calculated_Value) + ' United States Dollar')
def United_States_Yen():
    Input_Value = UI_set.TE_Input.toPlainText()
    Calculated_Value = float(Input_Value) * 105.84
    UI_set.TE_Output.setText(str(Calculated_Value) + ' Japanese Yen')
def Japanese_Won():
    Input_Value = UI_set.TE_Input.toPlainText()
    Calculated_Value = float(Input_Value) * 11.27
    UI_set.TE_Output.setText(str(Calculated_Value) + ' South Korean Won')
def South_Korean_Yen():
    Input_Value = UI_set.TE_Input.toPlainText()
    Calculated_Value = float(Input_Value) * 0.089
    UI_set.TE_Output.setText(str(Calculated_Value) + ' Japanese Yen')



def Calculate():
    print('d')





# pyinstaller로 원파일로 압축할때 경로 필요함

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainView()
    # main.show()
    sys.exit(app.exec_())