import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/main.nhn?code=005930"
result = requests.get(url)
bs_obj =BeautifulSoup(result.content, "html.parser")

# close 종가(전일)
no_today = bs_obj.find('td',{'class': 'first'}) # 태그 p, 속성값 no_today 찾기
blind = no_today.find('span', {'class': 'blind'}) # 태그 span, 속성값 blind 찾기
close = blind.text

th_data = [item.get_text().strip() for item in finance_html.select('thead th')]


