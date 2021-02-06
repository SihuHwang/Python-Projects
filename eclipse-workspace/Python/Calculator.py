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
        UI_set = QtUiTools.QUiLoader().load(resource_path("./Calculator.ui"))

        UI_set.BTN_0.clicked.connect(Number_0)
        UI_set.BTN_1.clicked.connect(Number_1)
        UI_set.BTN_2.clicked.connect(Number_2)
        UI_set.BTN_3.clicked.connect(Number_3)
        UI_set.BTN_4.clicked.connect(Number_4)
        UI_set.BTN_5.clicked.connect(Number_5)
        UI_set.BTN_6.clicked.connect(Number_6)
        UI_set.BTN_7.clicked.connect(Number_7)
        UI_set.BTN_8.clicked.connect(Number_8)
        UI_set.BTN_9.clicked.connect(Number_9)
        UI_set.BTN_Decimal.clicked.connect(Decimal)
        UI_set.BTN_Decimal.setEnabled(True)
        UI_set.BTN_Divide.clicked.connect(Divide)
        UI_set.BTN_Multiply.clicked.connect(Multiply)
        UI_set.BTN_Minus.clicked.connect(Minus)
        UI_set.BTN_Plus.clicked.connect(Plus)
        UI_set.BTN_Equal.clicked.connect(Equal)
        UI_set.BTN_Clear.clicked.connect(Clear)
        #         #enable or not
        #         UI_set.pushButton.setEnabled(True)
        #         UI_set.pushButton.setEnabled(False)
        #         #change background color
        #         UI_set.pushbutton.setStyleSheet('background color:#ffffff')
        self.setCentralWidget(UI_set)
        self.setWindowTitle("Calculator")
        # self.setWindowIcon(QtGui.QPixmap(resource_path("./images/bbok.png")))
        self.resize(348, 473)
        self.show()
    # 파일 경로

def Number_0():
    get = UI_set.LE_Result.text()
    UI_set.LE_Result.setText( get + str(0))
def Number_1():
    get = UI_set.LE_Result.text()
    UI_set.LE_Result.setText( get + str(1))
def Number_2():
    get = UI_set.LE_Result.text()
    UI_set.LE_Result.setText( get + str(2))
def Number_3():
    get = UI_set.LE_Result.text()
def Number_4():
    UI_set.LE_Result.setText( get + str(3))
    get = UI_set.LE_Result.text()
    UI_set.LE_Result.setText( get + str(4))
def Number_5():
    get = UI_set.LE_Result.text()
    UI_set.LE_Result.setText( get + str(5))
def Number_6():
    get = UI_set.LE_Result.text()
    UI_set.LE_Result.setText( get + str(6))
def Number_7():
    get = UI_set.LE_Result.text()
    UI_set.LE_Result.setText( get + str(7))
def Number_8():
    get = UI_set.LE_Result.text()
    UI_set.LE_Result.setText( get + str(8))
def Number_9():
    get = UI_set.LE_Result.text()
    UI_set.LE_Result.setText( get + str(9))
def Decimal():
    get = UI_set.LE_Result.text()
    UI_set.LE_Result.setText( get + '.')
    UI_set.BTN_Decimal.setEnabled(False)
def Divide():
    a = UI_set.LE_Result.text()
    b = UI_set.LB_Result.text()


    if a != "":
        UI_set.LB_Result.setText(b + a + ' / ')

    UI_set.LE_Result.setText('')
    UI_set.BTN_Decimal.setEnabled(True)

def Multiply():
    a = UI_set.LE_Result.text()
    b = UI_set.LB_Result.text()

    if a != "":
        UI_set.LB_Result.setText(b + a + ' * ')

    UI_set.LE_Result.setText('')
    UI_set.BTN_Decimal.setEnabled(True)
def Minus():
    a = UI_set.LE_Result.text()
    b = UI_set.LB_Result.text()

    if a != "":
        UI_set.LB_Result.setText(b + a + ' - ')

    UI_set.LE_Result.setText('')
    UI_set.BTN_Decimal.setEnabled(True)
def Plus():
    a = UI_set.LE_Result.text()
    b = UI_set.LB_Result.text()

    if a != "":
        UI_set.LB_Result.setText(b + a + ' + ')

    UI_set.LE_Result.setText('')
    UI_set.BTN_Decimal.setEnabled(True)
def Clear():
    UI_set.LE_Result.setText('')
    UI_set.LB_Result.setText('')
    UI_set.BTN_Decimal.setEnabled(True)
def Equal():
    a = UI_set.LE_Result.text()
    x = UI_set.LB_Result.text()

    if a != "":
        UI_set.LB_Result.setText(x + a)

    result = UI_set.LB_Result.text()
    resultlist = result.split(' ')
    sign = ""
    total = 0
    legnth = len(resultlist)

    for i in range(legnth):
        try:
            g = float(resultlist[i])
            if sign == '':
                total = g
            else:
                if sign == '/':
                    total = total / g
                elif sign == '*':
                    total = total * g
                elif sign == '+':
                    total = total + g
                elif sign == '-':
                    total = total - g

            UI_set.LE_Result.setText(str(total))

        except:
            sign = resultlist[i]

    UI_set.BTN_Decimal.setEnabled(True)


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