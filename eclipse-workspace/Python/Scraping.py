import requests
from bs4 import BeautifulSoup

result = requests.get('https://www.jbmpa.com/test/scraping.html')
html = result.text

BS = BeautifulSoup(html, 'html.parser')
# print(BS.head.title.text)

# print(BS.find_all('meta'))

# for resultMeta in BS.head.find_all('meta'):
#     print(resultMeta.get('content'))

# print(BS.head.find('meta', {'name':'application-name'}))
#
# print(BS.find(id='reference'))

# print(BS.head.find("meta", {"name": "application-name"}))
#
# print(BS.head.find("meta", {"name": "application-name"}).get('content'))
#
# print(BS.find("p", {"id": "title1"}))
# print(BS.find("p", {"id": "title1"}).text)

# for resultLink in BS.find_all('a'):
#     print(resultLink.text.strip())
#     print(resultLink.get('href'))
#
# print("\n###########################\n")
#
# for resultLink in BS.find("p", {"id": "reference"}).find_all('a'):
#     print(resultLink.text.strip())
#     print(resultLink.get('href'))

# for resultMeta in BS.head.find_all('meta'):
#     print(resultMeta.get('content'))
#
# print("\n###########################\n")
#
# for resultMeta in BS.head.select('meta'):
#     print(resultMeta.get('content'))
#
# se = BS.head.select('meta')[1]
# print(se)
# print(se.get('content'))

Tbody = BS.table.tbody

a = Tbody.find_all('tr')

for b in a:
    c = b.select('td')[3].text
    d = b.select('td')[4].text
    print(c,d)


