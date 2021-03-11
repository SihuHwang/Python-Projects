from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


# create a Window class
class Window(QMainWindow):
    # constructor
    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle('Tic Tac Toe Game')
        self.setWindowIcon(QtGui.QIcon('1_9LBDOx6gG4mTuPGPDp888w.png'))
        # setting geometry
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.resize(300, 500)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

        # method for components

    def UiComponents(self):

        # turn
        self.turn = 0

        # times
        self.times = 0

        # creating a push button list
        self.push = []

        # creating 2d list
        for _ in range(3):
            temp = []
            for _ in range(3):
                temp.append((QPushButton(self)))
                # adding 3 push button in single row
            self.push.append(temp)


            # x and y co-ordinate
        x = 90
        y = 90
        # traversing through push button list
        for i in range(3):
            for j in range(3):
                # setting geometry to the button
                self.push[i][j].setGeometry(x * i + 20,
                                                 y * j + 20,
                                                 80, 80)

                # setting font to the button
                self.push[i][j].setFont(QFont(QFont('Times', 17)))

                # adding action
                self.push[i][j].clicked.connect(self.start_game)

                # creating label to tel the score
        self.label = QLabel(self)

        # setting geometry to the label
        self.label.setGeometry(20, 300, 260, 60)

        # setting style sheet to the label
        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 3px solid lime;"
                                 "background : white;"
                                 "}")

        # setting label alignment
        self.label.setAlignment(Qt.AlignCenter)

        # setting font to the label
        self.label.setFont(QFont('Times', 15))

        # creating push button to restart the score
        reset_game = QPushButton("Reset-Game", self)

        # setting geometry
        reset_game.setGeometry(50, 380, 200, 50)


        # adding action action to the reset push button
        reset_game.clicked.connect(self.reset_game)

        # method called by reset button

    def reset_game(self):

        # resetting values
        self.turn = 0
        self.times = 0

        # making label text empty:
        self.label.setText("")

        # traversing push list
        for buttons in self.push:
            for button in buttons:
                # making all the button enabled
                button.setEnabled(True)
                # removing text of all the buttons
                button.setText("")

                # action called by the push buttons

    def start_game(self):

        self.times += 1

        # getting button which called the action
        button = self.sender()

        # making button disabled
        button.setEnabled(False)

        # checking the turn
        if self.turn == 0:
            button.setText("X")
            self.turn = 1
        else:
            button.setText("O")
            self.turn = 0

        # call the winner checker method
        win = self.winner()

        # text
        text = ""

        # if winner is decided
        if win == True:
            # if current chance is 0
            if self.turn == 0:
                # O has won
                text = "O Won"
            # X has won
            else:
                text = "X Won"

            # disabling all the buttons
            for buttons in self.push:
                for push in buttons:
                    push.setEnabled(False)

                    # if winner is not decided
        # and total times is 9
        elif self.times == 9:
            text = "Match is Draw"

        # setting text to the label
        self.label.setText(text)

        # method to check who wins

    def winner(self):

        # checking if any row crossed
        for i in range(3):
            if self.push[0][i].text() == self.push[1][i].text() \
                    and self.push[0][i].text() == self.push[2][i].text() \
                    and self.push[0][i].text() != "":
                return True

        # checking if any column crossed
        for i in range(3):
            if self.push[i][0].text() == self.push[i][1].text() \
                    and self.push[i][0].text() == self.push[i][2].text() \
                    and self.push[i][0].text() != "":
                return True

        # checking if diagonal crossed
        if self.push[0][0].text() == self.push[1][1].text() \
                and self.push[0][0].text() == self.push[2][2].text() \
                and self.push[0][0].text() != "":
            return True

        # if other diagonal is crossed
        if self.push[0][2].text() == self.push[1][1].text() \
                and self.push[1][1].text() == self.push[2][0].text() \
                and self.push[0][2].text() != "":
            return True

        # if nothing is crossed
        return False


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())