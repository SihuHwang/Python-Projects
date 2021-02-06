import sys
import os
import datetime
from PySide2 import QtUiTools, QtGui
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem
from PIL import Image
from PIL.ExifTags import TAGS

class MainView(QMainWindow):

    # __slots__ = ()
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.setButtons()
    def setupUI(self):
        global UI_MAIN, UI_REPLACE, UI_FRONT, UI_BACK
        UI_MAIN = QtUiTools.QUiLoader().load(resource_path("./filenamechange.ui"))
        UI_REPLACE = QtUiTools.QUiLoader().load(resource_path("./filenamechange_replace.ui"))
        UI_REPLACE.setWindowTitle('문자열 변경')
        UI_FRONT = QtUiTools.QUiLoader().load(resource_path("./filenamechange_front.ui"))
        UI_REPLACE.setWindowTitle('앞에 문자 추가')
        UI_BACK = QtUiTools.QUiLoader().load(resource_path("./filenamechange_back.ui"))
        UI_REPLACE.setWindowTitle('뒤에 문자 추가"')
        UI_MAIN.TW_list.setHorizontalHeaderLabels(['현재이름','변경이름','파일경로','파일크기','변경시각'])
        self.setCentralWidget(UI_MAIN)
        self.setWindowTitle("Vending Machine")
        # self.setWindowIcon(QtGui.QPixmap(resource_path("./images/bbok.png")))
        self.resize(917, 846)
        self.show()
    def setButtons(self):
        UI_MAIN.BTN_list.clicked.connect(self.FilesOpen)
        UI_MAIN.BTN_replace.clicked.connect(self.NameReplaceFormOn)
        UI_REPLACE.BTN_cancel.clicked.connect(self.NameReplaceFormOff)
        UI_REPLACE.BTN_confirm.clicked.connect(NameReplace)
        UI_MAIN.BTN_frontadd.clicked.connect(self.FrontaddFormOn)
        UI_FRONT.BTN_cancel.clicked.connect(self.FrontaddFormOff)
        UI_FRONT.BTN_confirm.clicked.connect(Frontadd)
        UI_MAIN.BTN_backadd.clicked.connect(self.BackaddFormOn)
        UI_BACK.BTN_cancel.clicked.connect(self.BackaddFormOFf)
        UI_BACK.BTN_confirm.clicked.connect(Backadd)
        UI_MAIN.BTN_exif.clicked.connect(ExifExcute)
        UI_MAIN.BTN_excute.clicked.connect(RenameExcute)
        UI_MAIN.BTN_cancel.clicked.connect(RenameReset)
        UI_MAIN.BTN_clear.clicked.connect(ClearRows)
        UI_MAIN.BTN_upper.clicked.connect(Upper)
        UI_MAIN.BTN_lower.clicked.connect(Lower)

    def FilesOpen(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFiles)
        dialog.setNameFilter(self.tr("Images(*.png *.xpm *.jpg *.gif);; All Files(*.*)"))
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec():
            fileNames = dialog.selectedFiles()
            setList(fileNames)
    def NameReplaceFormOn(self):
        UI_REPLACE.show()
    def NameReplaceFormOff(self):
        UI_REPLACE.close()
    def FrontaddFormOn(self):
        UI_FRONT.show()
    def FrontaddFormOff(self):
        UI_FRONT.close()
    def BackaddFormOn(self):
        UI_BACK.show()
        UI_BACK.activateWindow()
    def BackaddFormOFf(self):
        UI_BACK.close()

def Upper():
    rowcount = UI_MAIN.TW_list.rowCount()

    for i in range(rowcount):
        prevname = UI_MAIN.TW_list.item(i, 1).text()
        name = prevname.split('.')
        newname = name[0].upper()+ '.' + name[1]

        UI_MAIN.TW_list.item(i, 1).setText(newname)


def Lower():
    rowcount = UI_MAIN.TW_list.rowCount()

    for i in range(rowcount):
        prevname = UI_MAIN.TW_list.item(i, 1).text()
        name = prevname.split('.')
        newname = name[0].lower() + '.' + name[1]

        UI_MAIN.TW_list.item(i, 1).setText(newname)
def ClearRows():
    UI_MAIN.TW_list.setRowCount(0)
def RenameReset():
    rowcount = UI_MAIN.TW_list.rowCount()

    for i in range(rowcount):
        cname = UI_MAIN.TW_list.item(i, 0).text()
        UI_MAIN.TW_list.item(i, 1).setText(cname)

def RenameExcute():
    rowcount = UI_MAIN.TW_list.rowCount()
    for i in range(rowcount):
        dir = UI_MAIN.TW_list.item(i, 2).text()
        cname = UI_MAIN.TW_list.item(i, 0).text()
        newname = UI_MAIN.TW_list.item(i, 1).text()

        if cname != newname:
            result = os.rename(dir + "/" + cname, dir + "/" + newname)
            UI_MAIN.TW_list.item(i, 0).setText(newname)

def ExifExcute():
    rowcount = UI_MAIN.TW_list.rowCount()
    for i in range(rowcount):
        cname = UI_MAIN.TW_list.item(i, 0).text()
        tempname = cname.split(".")
        dir = UI_MAIN.TW_list.item(i, 2).text()

        try:
            filename = dir + '/' + cname
            image = Image.open(filename)
            info = image.getexif()
            image.close()


            if info != None:
                taglabel = {}

                for tag, value in info.items():
                    decoded = TAGS.get(tag, tag)
                    taglabel[decoded] = value


                newname = taglabel['DateTimeOriginal'].replace(":","")
                newname = newname.replace("-","")
                newname = newname.replace(" ","_") + '.' + tempname[1]
                UI_MAIN.TW_list.item(i, 1).setText(newname)
            else:
                pass
        except:
            pass

def Backadd():
    str_new = UI_BACK.LE_str.text()
    rowcount = UI_MAIN.TW_list.rowCount()
    for i in range(rowcount):
        prevname = UI_MAIN.TW_list.item(i, 1).text()

        tempname = prevname.split(".")
        newname = tempname[0] + str_new + "." + tempname[1]

        UI_MAIN.TW_list.item(i, 1).setText(newname)

    UI_BACK.close()
def Frontadd():
    str_new = UI_FRONT.LE_str.text()
    rowcount = UI_MAIN.TW_list.rowCount()

    for i in range(rowcount):
        prevname = UI_MAIN.TW_list.item(i, 1).text()
        newname = str_new + prevname


        UI_MAIN.TW_list.item(i, 1).setText(newname)

    UI_FRONT.close()
def NameReplace():
    str_prev = UI_REPLACE.LE_prev.text()
    str_new = UI_REPLACE.LE_new.text()

    rowcount = UI_MAIN.TW_list.rowCount()

    for i in range(rowcount):
        prevname = UI_MAIN.TW_list.item(i, 1).text()
        newname = prevname.replace(str_prev, str_new)

        UI_MAIN.TW_list.item(i, 1).setText(newname)

    UI_REPLACE.close()

def setList(fileNames):
    precount = UI_MAIN.TW_list.rowCount()




    for i in range(precount):
        p = UI_MAIN.TW_list.item(i, 2).text() + '/' + UI_MAIN.TW_list.item(i, 0).text()
        if p in fileNames:
            fileNames.remove(p)

    count = len(fileNames)

    UI_MAIN.TW_list.setRowCount(precount + count)


    for i in range(count):
        dir, file = os.path.split(fileNames[i])
        fsize = os.path.getsize(fileNames[i])
        mtime = os.path.getmtime(fileNames[i])

        mtimesstamp = datetime.datetime.fromtimestamp(int(mtime))

        UI_MAIN.TW_list.setItem(i + precount, 0, QTableWidgetItem(file))
        UI_MAIN.TW_list.setItem(i + precount, 1, QTableWidgetItem(file))
        UI_MAIN.TW_list.setItem(i + precount, 2, QTableWidgetItem(dir))
        UI_MAIN.TW_list.setItem(i + precount, 3, QTableWidgetItem(str(fsize)))
        UI_MAIN.TW_list.setItem(i + precount, 4, QTableWidgetItem(str(mtimesstamp)))

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