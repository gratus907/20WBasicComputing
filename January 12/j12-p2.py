from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/exchangeList.nhn'
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

info = soup.find_all('td')
for i in range(len(info)):
    if i % 7 == 0:
        print()
    print(info[i].string.strip(), end = ' ')