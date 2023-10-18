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
    detail_url = 'https://stock.mk.co.kr/price/home/'+code
    
    response = requests.get(detail_url)
    html = response.text
    soup = BeautifulSoup(html,'html.parser')
    
    trading_valume = soup.select_one('#trading_valume').text.strip()
    acmount = soup.select_one('#transaction_acmount').text.strip()
    capital = soup.select_one('.noline_bottom > tbody > tr:nth-child(3) > td:nth-child(2) > span').text.strip()
    number = soup.select_one('.noline_bottom > tbody > tr:nth-child(4) > td:nth-child(2) > span').text.strip()
    total = soup.select_one('.noline_bottom > tbody > tr:nth-child(5) > td:nth-child(2) > span').text.strip()
    foreigners = soup.select_one('.noline_bottom > tbody > tr:nth-child(6) > td:nth-child(2) > span').text.strip().replace("%","").strip()
    per = soup.select_one('.noline_bottom > tbody > tr:nth-child(7) > td:nth-child(2) > span').text.split("/")[0].strip()
    eps = soup.select_one('.noline_bottom > tbody > tr:nth-child(7) > td:nth-child(2) > span').text.split("/")[1].strip()
    
    print(idx,code,name,trading_valume,acmount,capital,number,total,foreigners,per,"/",eps)
   


