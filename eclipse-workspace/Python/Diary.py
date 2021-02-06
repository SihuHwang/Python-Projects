import sys
import os
import sqlite3 as sq
from PySide2 import QtUiTools,  QtCore, QtGui
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox


class MainView(QMainWindow):

    # __slots__ = ()
    def __init__(self):
        super().__init__()

        Create_Table()
        self.setupUI()

    def setupUI(self):
        global UI_set
        UI_set = QtUiTools.QUiLoader().load(resource_path("./diary.ui"))

        UI_set.BTN_Save.clicked.connect(Diary_Save)
        UI_set.Calendar.clicked.connect(SelectDate)
        UI_set.CB_SavedDiary.currentIndexChanged.connect(Insert_Content)
        UI_set.Calendar.currentPageChanged.connect(Changed_Date)
        #         #enable or not
        #         UI_set.pushButton.setEnabled(True)
        #         UI_set.pushButton.setEnabled(False)
        #         #change background color
        #         UI_set.pushbutton.setStyleSheet('background color:#ffffff')
        #
        self.setCentralWidget(UI_set)
        self.setWindowTitle("Diary")
        # self.setWindowIcon(QtGui.QPixmap(resource_path("./images/bbok.png")))
        self.resize(851, 604)
        self.show()

        Saved_Diary()
    # 파일 경로


def insertDate(savedate):
    conn = sq.connect('Database_Diary.db')
    cur = conn.cursor()

    sql = "SELECT date FROM diary WHERE date like '"+savedate +"%' order by date"
    cur.execute(sql)
    rows = cur.fetchall()
    count = len(rows)

    UI_set.CB_SavedDiary.clear()

    for i in rows:
        UI_set.CB_SavedDiary.addItem(i[0])

def messageBox(msg,title):
        msgBox = QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setWindowIcon(QtGui.QPixmap("info.png"))
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(msg)
        # msgBox.setInformativeText('Your Diary for today has been saved')
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setDefaultButton(QMessageBox.Ok)

        # 클릭한 버튼의 결과를 int로 반환한다.

        return msgBox.exec_()


def Saved_Diary():

    date = UI_set.Calendar.selectedDate()
    savedate = date.toString('yyyy-MM')

    insertDate(savedate)



def Changed_Date(year,month):

    strmonth = str(month).rjust(2, '0')
    savedate = str(year) + '-' + strmonth

    insertDate(savedate)


def SelectDiary(date):
    conn = sq.connect('Database_Diary.db')
    cur = conn.cursor()

    sql = "SELECT * FROM diary WHERE date =  '" + date + "'"
    cur.execute(sql)
    rows = cur.fetchall()

    count = len(rows)
    # print(count)
    if count > 0:
        idx = rows[0][0]
        date = rows[0][1]
        content = rows[0][2]
        time_w = rows[0][3]
        time_s = rows[0][4]
        weather = rows[0][5]

        UI_set.CB_Weather.setCurrentText(weather)
        UI_set.TE_Content.setText(content)

        UI_set.CB_SavedDiary.setCurrentText(date)

        time_w_temp = time_w.split(':')
        UI_set.Time_W.setTime(QtCore.QTime(int(time_w_temp[0]), int(time_w_temp[1]), int(time_w_temp[2])))

        time_s_temp = time_s.split(':')
        UI_set.Time_S.setTime(QtCore.QTime(int(time_s_temp[0]), int(time_s_temp[1]), int(time_s_temp[2])))

        # print(rows)
        # print(idx, date, content,time_w, time_s, weather)

    else:
        UI_set.TE_Content.setText(' ')
        # print('a')









def Insert_Content():
    date = UI_set.CB_SavedDiary.currentText()
    SelectDiary(date)

def SelectDate():

    date = UI_set.Calendar.selectedDate()
    savedate = date.toString('yyyy-MM-dd')

    UI_set.CB_SavedDiary.setCurrentText(savedate)

    SelectDiary(savedate)



def Diary_Save():

    date = UI_set.Calendar.selectedDate()
    savedate = date.toString('yyyy-MM-dd')
    weather = UI_set.CB_Weather.currentText()
    time_w =  UI_set.Time_W.time().toString()
    time_s = UI_set.Time_S.time().toString()
    content = UI_set.TE_Content.toPlainText()
    Insert_Data(savedate, content, time_w, time_s, weather)

    messageBox('Your Diary for today has been saved','SAVED')
def Create_Table():
    conn = sq.connect('Database_Diary.db')
    cur = conn.cursor()

    sql = 'create table diary(idx INTEGER PRIMARY KEY,' \
          ' date varchar(10),' 'content TEXT,' 'time_w varchar(10),' \
          'time_s varchar(10),' \
          ' weather varchar(15) )'

    try:
        cur.execute(sql)
        conn.commit()

    except:
        pass



    conn.close()
def Insert_Data(savedate, content, time_w, time_s, weather):


    conn = sq.connect('Database_Diary.db')
    cur = conn.cursor()

    sql = "SELECT idx FROM diary WHERE date =  '" + savedate + "'"
    cur.execute(sql)
    rows = cur.fetchall()

    count = len(rows)

    if count > 0:
        sql = "UPDATE diary set date = ?, content = ?, time_w = ?, time_s = ?, weather = ? WHERE date =  '" \
              "" + savedate + "'"
        cur.execute(sql, (savedate, content, time_w, time_s, weather))
        conn.commit()

    else:
        sql = 'INSERT into diary (date, content, time_w, time_s, weather) ' \
              'values (?,?,?,?,?)'

        cur.execute(sql, (savedate, content, time_w, time_s, weather))
        conn.commit()

    conn.close()

    Saved_Diary()

    UI_set.CB_SavedDiary.setCurrentText(savedate)
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






