'''
Created on Nov 14, 2019

@author: sihuh
'''





# while True:
#     try:
#     
#         input('input number:'))
#         
#         if number >= 10 or number <=        1:
#             print('Please enter number 2 ~ 9')
#         else:
#             for i in range(1,10):
#                 print('%s X %s is' %(number, i), number * i)
#     
#     except:
#         
#         print('Please enter a number')
#         



# cola_price = 10
# cola_count = 5
# dew_price = 8
# dew_count = 5
# vending = True
# 
# def showcount():
#     print('%s cola is left' % cola_count)
#     print('%s Dew is left' % dew_count)
# 
# 
#        
# 
# while vending:
#    
#    
#     
#      try:
#          
#             
#             cola_count = cola_count - 1
#             dew_count = dew_count - 1
#             
#             drink = input('what drink? Cola or Dew:')
#             
#             
#             
#             money = int(input('insert money:'))
#             
#             
#             if drink == 'cola' or 'Cola' and money >= cola_price  :
#                 print(' here is your Cola')
#                 
#             
#             
#             if drink ==  'dew' or 'Dew' and money >= dew_price :
#                 print('here is your dew')
#             else:
#                 print('you do not have enough money') 
#             
#             if cola_count == 0:
#                 print('We are out of Cola')
#                 vending = False 
#             
#             if dew_count == 0:
#                 print('We are out of Dew')
#             
#             
#         
#         
#      except:
#         print('Please insert Money')
#     
#     
   
        #print('Money is only accepted')          


cola_price = 10
cola_count = 5
dew_price = 8
dew_count = 5
vending = True
Database = {'cola_price':10, 'cola_count':5, 'dew_price':8, 'dew_count':5}
try:
    f = open('Database-vending.txt','r')
    data = f.readline()
    
    f.close()
except:
    f = open('Database-vending.txt','w')
    f.write(str(Database))
    f.close()
print(data)


Database = eval(data)
def remain_count():
    print('cola %s left'% Database.get('cola_count'))
    print('dew %s left'% Database.get('dew_count'))

    
while vending:

    try:
        drink = input('Cola or Dew? :')
    except:
        print('Please choose Cola or Dew')
        continue

    try:
        money = float(input('Insert Money :'))

        if drink.lower() == 'cola':
            if Database.get('cola_count') > 0:
                if money >= Database.get('cola_price'):
                    print('you have enough money, and here is your Cola')
                    Database['cola_count'] = Database.get('cola_count') - 1
                    remain_count()

                else:
                    print('you do not have enough money')
            else:
                print('We are out of Cola')
                continue

        elif drink.lower() == 'dew':
            if Database.get('dew_count') > 0:
                if money >= Database.get('dew_price'):
                    print('you have enough money, here is your Dew')
                    Database['dew_count'] = Database.get(dew_count) - 1
                    remain_count()
                else:
                    print('you do not enough money')
            else:
                print('We are out Dew ')
                continue
    

    except:
        print('Please insert money only')
