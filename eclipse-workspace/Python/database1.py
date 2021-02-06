'''
Created on Jun 25, 2019

@author: sihuh
'''

import sys
import os
import sqlite3 as sq
from PySide2 import QtUiTools, QtGui
from PySide2.QtWidgets import QApplication, QMainWindow, QTableWidgetItem ,QHeaderView

 

#database 이름 설정
Databasename = "nametable.db"


class MainView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

 

    def setupUI(self):
        global UI_set


        #UI 파일 로딩
        UI_set = QtUiTools.QUiLoader().load(resource_path("database.ui"))
        
        #버튼 클릭시 데이터 입력을 위해 연결할 클래스 외부 함수
        UI_set.BTN_Insert.clicked.connect(InsertData)
        
        #Table의 내부 셀을 클릭할 때 연결할 클래스 외부 함수
        #셀을 클릭하여 연결한 함수에는 기본적으로 셀의 Row, Column 두개의 인자를 넘겨준다.
        UI_set.tableWidget.cellClicked.connect(DeleteData)
                
        #Table 기본 세팅위해 내부 메서드 호출
        self.setTable()
                        
        #데이터베이스 세팅을 위해 외부 함수 호출
        CreateTable()
        
        #데이터베이스 세팅 후, DB 값 불러오기외부 함수 호출
        SelectData()
                
        # GUI 화면 출력
        self.setCentralWidget(UI_set)
        self.setWindowTitle("GUI Program Test")
        self.setWindowIcon(QtGui.QPixmap(resource_path("./images/jbmpa.png")))
        self.resize(917,846)
        self.show()
        
        
    def setTable(self):
        #Table 가로(column) 갯수
        UI_set.tableWidget.setColumnCount(4)
        
        #Table 칼럼 헤더 라벨
        UI_set.tableWidget.setHorizontalHeaderLabels(['번호','이름','나이','삭제'])

 

def CreateTable():
    #sqlite3 db 파일 접속, 없으면 생성
    conn = sq.connect(Databasename)
    cur = conn.cursor()
    
    #db에 aaa라는 테이블이 있는지 sqlite3의 마스터 테이블에서 정보를 받아온다.
    sql = "SELECT name FROM sqlite_master WHERE type='table' AND name ='aaa'"
    cur.execute(sql)
    rows = cur.fetchall()
        
    #aaa 테이블이 없으면 새로 생성하고,  있으면 통과
    if not rows:        
        sql = "CREATE TABLE aaa (idx INTEGER PRIMARY KEY, name TEXT, age INTEGER)"
        cur.execute(sql)
        conn.commit()
    
    conn.close()
    
def InsertData():
    #두개의 lineEdit에서 각각 이름과 나이를 받아온다.  
    name = UI_set.lineEdit.text()
    age = UI_set.lineEdit_2.text()
    
    conn = sq.connect(Databasename)
    cur = conn.cursor()
    
    sql = "INSERT INTO aaa (name, age) VALUES (?,?)"
    cur.execute(sql, (name, age))
    conn.commit()
    
    conn.close()
    
    #데이터 입력 후 DB의 내용 불러와서 TableWidget에 넣기 위한 함수 호출
    SelectData()
    
    
def DeleteData(row, column):
    #테이블 내부의 셀 클릭과 연결된 이벤트는 기본적으로 셀의 Row, Column을 인자로써 전달받는다.
    
    #삭제 셀이 눌렸을 때, 삭제 셀은 4번째 셀이므로 column 값이 3일 경우만 작동한다.
    if column == 3: 
        conn = sq.connect(Databasename)
        cur = conn.cursor()
        
        #DB의 데이터 idx는 선택한 Row의 첫번째 셀(0번 Column)의 값에 해당한다.
        idx = UI_set.tableWidget.item(row, 0).text()
        
        sql = "DELETE FROM aaa WHERE idx =?"
        cur.execute(sql, (idx,))
        conn.commit()
        
        conn.close()
        
        #데이터 삭제 후 DB의 내용 불러와서 TableWidget에 넣기 위한 함수 호출
        SelectData()
    
def SelectData():
    #데이터베이스 내부 테이블의 내용을 모두 추출
    conn = sq.connect(Databasename)
    cur = conn.cursor()
    
    sql = "SELECT * FROM aaa"
    cur.execute(sql)
    rows = cur.fetchall()        
    
    conn.close()
    
    #DB의 내용을 불러와서 TableWidget에 넣기 위한 함수 호출
    setTables(rows)


def setTables(row):
    #DB내부에 저장된 결과물의 갯수를 저장한다.        
    count = len(row)
    
    #갯수만큼 테이블의 Row를 생성한다.
    UI_set.tableWidget.setRowCount(count)
    
    #row 리스트만큼 반복하며 Table에 DB 값을 넣는다.
    for x in range(count):
        #리스트 내부의 column쌍은 튜플로 반환하므로 튜플의 각 값을 변수에 저장
        idx, name, age = row[x]
           
        #테이블의 각 셀에 값 입력
        UI_set.tableWidget.setItem(x, 0, QTableWidgetItem(str(idx)))
        UI_set.tableWidget.setItem(x, 1, QTableWidgetItem(name))
        UI_set.tableWidget.setItem(x, 2, QTableWidgetItem(str(age)))
        UI_set.tableWidget.setItem(x, 3, QTableWidgetItem("삭제"))        
    
        UI_set.tableWidget.setRowHeight(x , 150)
    
    UI_set.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
    UI_set.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

       
       
    UI_set.tableWidget.setColumnWidth(1 ,125)
    UI_set.tableWidget.setColumnWidth(2 ,125)
    UI_set.tableWidget.setColumnWidth(3 ,125)
       


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