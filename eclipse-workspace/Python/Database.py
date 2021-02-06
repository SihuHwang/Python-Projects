'''
Created on Jun 18, 2019

@author: sihuh
'''
import sqlite3 as sq




def CreateTable():
    conn = sq.connect("AAA.db")
    cur = conn.cursor()


    #AAA.db에 aaa라는 테이블이 있는지 sqlite3의 마스터 테이블에서 정보를 받아온다.
    sql = "SELECT name FROM sqlite_master WHERE type='table' AND name ='aaa'"
    cur.execute(sql)
    rows = cur.fetchall()
                                                                                        
    #aaa 테이블이 없으면 새로 생성하고 있으면 통과
    if not rows:        
        sql = "CREATE TABLE aaa (idx INTEGER PRIMARY KEY, name TEXT, age INTEGER)"
        cur.execute(sql)
        conn.commit()
    
    conn.close()
    
def InsertData(name, age):    
    conn = sq.connect("AAA.db")
    cur = conn.cursor()
    
    sql = "INSERT INTO aaa (name, age) VALUES (?,?)"
    cur.execute(sql, (name, age))
    conn.commit()
    
    conn.close()
    
def UpdateName(name, idx):    
    conn = sq.connect("AAA.db")
    cur = conn.cursor()
    
    sql = "UPDATE aaa set name=? WHERE idx = "+str(idx)
    cur.execute(sql, (name,))
    conn.commit()
    
    conn.close()
    
def DeleteData(idx):    
    conn = sq.connect("AAA.db")
    cur = conn.cursor()
    
    sql = "DELETE FROM aaa WHERE idx =?"
    cur.execute(sql, (idx,))
    conn.commit()
    
    conn.close()
    
def SelectData():
    conn = sq.connect("AAA.db")
    cur = conn.cursor()
    
    sql = "SELECT * FROM aaa"
    cur.execute(sql)    
    rows = cur.fetchall()        
    
    conn.close()
    
    return rows


# 데이터베이스 테스트
CreateTable()
InsertData("Maru", 8)
InsertData("Seulchan", 7)
InsertData("Sun", 10)
InsertData("Moon", 14)
print(SelectData())

 

UpdateName("Maru Jung", 1)
print(SelectData())

 

DeleteData(3)
print(SelectData())