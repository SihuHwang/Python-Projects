'''
Created on Oct 9, 2019

@author: sihuh
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup


'''html = urlopen('http://kyobobook.co.kr/bestSellerNew/bestseller.laf')
bsObject = BeautifulSoup(html, 'html.parser')


book_page_urls = []
for cover in bsObject.find_all('div',{'class':'detail'}):
    link= cover.select('a')[0].get('href')
    book_page_urls.append(link)
    
print(book_page_urls)

for index, book_page_url in enumerate(book_page_urls):
    html= urlopen(book_page_url)
    bsObject = BeautifulSoup(html, 'html.parser')
    title = bsObject.find('meta',{'property':'rb:itemName'}).get('content')
    author = bsObject.select('span.name a')[0].text
    image = bsObject.find('meta', {'property':'rb:originalPrice'}).get('content')
    url = bsObject.find('meta',{'property':'rb:itemUrl'}).get('content')
    originalPrice = bsObject.find('meta',{'property':'rb:originalPrice'}).get('content')
    salePrice = bsObject.find('meta',{'property':'rb:salePrice'}).get('content')
    
    print(index+1, title, author, image, url, originalPrice, salePrice)'''
    
    
    
    
html = urlopen('https://www.ovitii.com/library/')
bsObject = BeautifulSoup(html, 'html.parser')


for cover in bsObject.find_all('div',{'class':'caption'}):
    title = cover.find('span',{'class':'listtitle'}).text

    print(title)
    
    

    
    



   