import requests
from bs4 import BeautifulSoup

url = 'https://stock.mk.co.kr/domestic/all_stocks'

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
lis = soup.select('.row_sty')
for idx,li in enumerate(lis):
    name = li.select_one('.name > a').text.strip()
    code = li.select_one('.name > a')['href']
    code = code[code.rindex("/")+1:]
    price = li.select_one('.price').text
    print(idx,code,name,price)
   


