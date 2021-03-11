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
        UI_set = QtUiTools.QUiLoader().load(resource_path("./Guess_number.ui"))
        self.result = []
        UI_set.BTN_Start.clicked.connect(self.start)
        UI_set.file.clicked.connect(self.file)
        UI_set.playerguess.setFocus()
        self.guesses = 0
#         #enable or not
#         UI_set.pushButton.setEnabled(True)
#         UI_set.pushButton.setEnabled(False)
#         #change background color
#         UI_set.pushbutton.setStyleSheet('background color:#ffffff')
#
        self.setCentralWidget(UI_set)
        self.setWindowTitle("Number Guessing Game")
        #self.setWindowIcon(QtGui.QPixmap(resource_path("./images/bbok.png")))
        self.resize(456,383)
        self.show()


    def start(self):
        self.guesses += 1
        try:
            number = random.randint(1,50)
            player = int(UI_set.playerguess.text())

            if player < 1 or player > 50:
                UI_set.result.setText('Please enter a number from 1 -100!')
                self.guesses = self.guesses - 1
            elif player < number:
                UI_set.result.setText('Your number was too low!')
                UI_set.guess.setText('Guess: %d' % self.guesses)
            elif player > number:
                UI_set.result.setText('Your number was too high!')
                UI_set.guess.setText('Guess: %d' % self.guesses)
            elif player == number:
                UI_set.result.setText('Correct!, you did it in %d guesses!' % self.guesses)
                if self.guesses == 1:
                    UI_set.result.setText('Correct!, you did it in %d guess!' % self.guesses)


        except:
            self.guesses = self.guesses - 1
            UI_set.result.setText('Please enter a number!')
            UI_set.playerguess.setText('')
            UI_set.playerguess.setFocus()



        resultstr = {'Number of Guesses':self.guesses}
        self.result.append(resultstr)
            # time.sleep(3)
            # sys.exit()

    def file(self):
        f = open('Guessing_number_results.txt', 'a')

        count = len(self.result)
        for x in range(count):
            f.write(str(self.result[x]) + '\n')
        f.close()




def resource_path(relative_path):

    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = MainView()
    #main.show()
    sys.exit(app.exec_())