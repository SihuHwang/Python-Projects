#1
print('Hello World ')

#2
print("Mary's cosmetics")

#3
print('신씨가 소리질렀다. "도둑이야".')

#4
print('C:\Windows')

#5
print("안녕하세요.\n만나서\t\t반갑습니다.")

#6
print ("오늘은", "일요일")

#7
print('naver;kakao;sk;samsung')

#8
print('naver/kakao/sk/samsung')

#9
print('first' ,end= ' ')
print('second')

#10
string = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"
print(len(string))

#11
a = "3"
b = "4"
print(a + b)

#12
s = "hello"
t = "python"
print(s + '!' + t)

#13
print("Hi" * 3)

#14
for i in range(80):
    print('-', end = '')
print(' ')
print('-' * 80)

#15
t1 = 'python'
t2 = 'java'

print((' '+ t1 + ' ' + t2)*4)

#16
price = 20,000
count = 10
print(price * count)

#17
2 + 2 * 3

#18
a = 128
print (type(a))

#19
num_str = "720"
print(int(num_str))

#20
num = 100
print(str(num))

#21
lang = 'python'
print(lang[0])
print(lang[2])

#22
license_plate = "24가 2210"
print(license_plate[4:])

#23
string = "홀짝홀짝홀짝"
print(string[0], end = '')
print(string[2] , end = '')
print(string[4])

#24
string = "PYTHON"
print(string[::-1])

#25
phone_number = "010-1111-2222"
print(phone_number.replace('-',' '))

#26
print(phone_number.replace('-',''))

#27
url = "http://sharebook.kr"
print(url[-2:])

#28
# lang = 'python'
# lang[0] = 'P'
# print(lang)

#29
string = 'abcdfe2a354a32a'
s = string.replace('a', 'A')
print(s)

#30
string = 'abcd'
a = string.replace('b', 'B')
print(a)

#41
movie_rank = ['닥터 스트레인지','스플릿','럭키']
# print(movie_rank)

#42
movie_rank.append('배트맨')
# print(movie_rank)

#43
movie_rank.insert(1,'슈퍼맨' )
# print(movie_rank)

#44
movie_rank.remove('럭키')
print(movie_rank)

#45
movie_rank.remove('스플릿')
movie_rank.remove('배트맨')
print(movie_rank)

#46
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
c = lang1 + lang2
print(c)

#47
nums = [1, 2, 3, 4, 5, 6, 7]
print(max(nums))
print(min(nums))

#48
nums = [1, 2, 3, 4, 5]
print(sum(nums))

#49
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))

#50
nums = [1, 2, 3, 4, 5]
print(sum(nums)/len(nums))

#51
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

#52
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print (nums[::2])

#53
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print (nums[1::2])

#54
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

#55
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

#56
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(interest[0], interest[1], interest[2], interest[3], interest[4])

#57
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print('/'.join(interest))

#58
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("\n".join(interest))

#59
string = "삼성전자/LG전자/Naver"
interest = [string[0:4], string[5:9], string[10:15]]
print(interest)

#60
string = "삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우"
interest = string.split('/')
print(interest)

#61
interest_0 = ['삼성전자', 'LG전자', 'SK Hynix']
interest_1 = interest_0
interest_1[0] = 'Naver'
print(interest_0)

#62
interest_0 = ['삼성전자', 'LG전자', 'SK Hynix']
interest_1 = interest_0[:2]
interest_1[0] = 'Naver'
print(interest_0)

#63
my_variable = ()

#64
t = (1, 2, 3)


#65
a = (1)

#66
t = 1, 2, 3, 4

#67
t = ('a', 'b', 'c')
t = (t[0].upper(), t[1], t[2])
print(t)

#68
interest = ('삼성전자', 'LG전자', 'SK Hynix')
l = list(interest)
print(l)

#69
interest = ['삼성전자', 'LG전자', 'SK Hynix']
m = tuple(interest)
print(m)

#70
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a + b + c)

#71
a, b, *c = (0, 1, 2, 3, 4, 5)

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

*valid_score, _, _= scores

#72
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_, _, *valid_score = scores

#73
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_, *valid_score, _ = scores

#74
temp = {}

#75
v = {'메로나':1000, '폴라포':1200, '빵빠레':1800}

#76
v['죠스바'] = 1200
v['월드콘'] = 1500
print(v)

#77
print("메로나 가격:", v['메로나'])

#78
v['메로나'] = 1300

#79
# del v['Melona']

#80
# icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# icecream['누가바']

#81
inventory = {'메로나': [300, 20], '비비빅': [400, 3], '죠스바': [250, 100]}
print(inventory)

#82
print(inventory['메로나'][0])

#83
print(inventory['메로나'][0])

#84
inventory['월드콘'] = [500, 7]
print(inventory)

#85
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(list(icecream.keys()))

#86
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(list(icecream.keys()))

#87
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(sum(icecream.values()))

#88
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)

#89
keys = ('apple', 'pear', 'peach')
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print(result)

#90
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

b = dict(zip(date, close_price))
print(b)

