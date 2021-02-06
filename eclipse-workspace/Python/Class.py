'''
Created on Jun 4, 2019

@author: sihuh
'''
class Book:
    def __init__(self,title):
        self.title = title
        self.price
        self.publisher 
        self.year
    
    def price(self,price):
        self.price = price
    
    def publisher(self, publisher):
        self.publisher = publisher  
    
    
    
    def year(self,year):
        self.year = year
        
    def getBook(self):
        bookinfo = "Book Title : " + self.title + ", publisher :  " + self.publisher + ", Year of publication :  " + self.year + ", price :  " + self.price    
        
        return bookinfo


a = Book('It is destiny')
b = Book('Move a foolish mountain')

a.publisher("A person's world")
a.year('2010')
a.price('13500')
ainfo = a.getBook()

b.publisher('Roh Moo-hyun Foundation')
b.year('2015')
b.price('15000')
binfo = b.getBook()
print(binfo)
print(ainfo)

