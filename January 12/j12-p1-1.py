from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cur'
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

names = soup.find_all('div', 'tit5')
scores = soup.find_all('td', 'point')
for name, score in list(zip(names, scores)):
    print(name.get_text().strip(), end = ' ')
    print(score.get_text().strip())