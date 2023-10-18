import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:8000/emp_list'

response = requests.get(url)

html = response.text
#BeautifulSoup는 text에서 '태그' 단위로 뽑아와 줄 수 있는 기능을 가지고있다.
soup = BeautifulSoup(html, 'html.parser')
trs = soup.select('tr')

for idx,tr in enumerate(trs):
    if idx == 0:
        continue
    tds = tr.select('td')
    print(tds[1].text,tds[3].text)

