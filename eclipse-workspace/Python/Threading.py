import threading
import time

class BackThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        #self.daemon = True
    
    def run(self):
        for i in range(50):
            print(threading.currentThread().getName, i)
            time.sleep(0.1)





def threadingtest1():
    for i in range(50):
        print(threading.currentThread().getName,i)
        time.sleep(0.1)

def threadingtest2():
    for i in range(50):
        print(threading.currentThread().getName, i) 
        time.sleep(0.1)     
        
thread1 = threading.Thread(target=threadingtest1 , args=())

thread2 = threading.Thread(target=threadingtest2 , args=())   



thread1.start()
thread2.start()
BackThread().start()