import requests
from bs4 import BeautifulSoup

url = "https://news.yahoo.co.jp/"
r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')


# 検索
for a in soup.find_all('a'):
      print(a.text)
      print(a.get('href'))