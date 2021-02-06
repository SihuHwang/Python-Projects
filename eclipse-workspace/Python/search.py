'''
Created on Oct 2, 2019

@author: sihuh
'''
import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.naver.com")
html = result.text


BS = BeautifulSoup(html, "html.parser")

'''
for meta in BS.head.find_all('meta'):   
    print(meta.get('content'))'''
    
for link in BS.find_all('a'):
    print(link.text,link.get('href'))

print(BS.head.find('meta',{'name':'description'}).get('content'))
