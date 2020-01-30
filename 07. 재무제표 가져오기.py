import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/main.nhn?code=005930"
result = requests.get(url)
html = result.text

soup = BeautifulSoup(html,'html.parser')

finance_html = soup.select('div.section.cop_analysis div.sub_section')
print(finance_html)