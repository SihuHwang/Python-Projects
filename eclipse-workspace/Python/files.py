
'''
Created on Nov 21, 2019

@author: sihuh
'''


f = open('files.txt', 'r')

# data = 'I am Sihu 2 \n'
# data = f.read()
# print(data)
# f.close()


# 
# while True:
#     data =  f.readline()
#     if data:
#         print(data)
#     else:
#         break


data = f.readlines()
print(data)

for i in data:
    print(i, end = '')

f.close

