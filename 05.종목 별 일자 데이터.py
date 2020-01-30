code = '005930'
import requests
url = 'http://finance.naver.com/item/sise_day.nhn?code={code}'.format(code=code)
res = requests.get(url)
res.encoding = 'utf-8'

# 위에서 수집한 데이터로 Beautiful soup 인스턴스 생성
from bs4 import BeautifulSoup
soap = BeautifulSoup(res.text, 'lxml')

el_table_navi = soap.find('table', class_ ='Nnavi')
el_td_last = el_table_navi.find('td', class_='pgRR')
pg_last = el_td_last.a.get('href').rsplit('&')[1]
pg_last = pg_last.split('=')[1]
pg_last = int(pg_last)
# print(pg_last) 마지막 페이지 출력력

import traceback
import pandas as pd

def parse_page(code,page):
    try:
        url = 'http://finance.naver.com/item/sise_day.nhn?code={code}&page={page}'.format(code=code, page=page)
        res = requests.get(url)
        _soap = BeautifulSoup(res.text, 'lxml')
        _df = pd.read_html(str(_soap.find('table')), header=0)[0]
        _df = _df.dropna()
        return _df
    except Exception as e:
        traceback.print_exc()
    return None

if __name__ == '__main__':
    # print(parse_page(code,1))


    for page in range(1,200):
        _df = parse_page(code,page)
        print(_df)
























# import pandas as pd
# import requests
# from bs4 import BeautifulSoup
#
# # 종목 이름을 입력하면 종목에 해당하는 코드를 불러와
# # 네이버 금융에 넣어줌
#
# def get_code_daily_price(company_code):
#     url = "https://finance.naver.com/item/sise_day.nhn?code=" + company_code
#     result = requests.get(url)
#     code_daily_price = BeautifulSoup(result.content, "html.parser")
#     return code_daily_price
#
# def get_daily_price(company_code):
#     code_daily_price = get_code_daily_price(company_code)
#
#
#
#
#
#
# if __name__ == '__main__':
#     url = '005930'
#
#     # 일자 데이터를 담을 df라는 DataFrame 정의
#     df = pd.DataFrame()
#
#     # 1페이지에서 20페이지의 데이터만 가져오기
#     for page in range(1, 21):
#         pg_url = '{url}&page={page}'.format(url=url, page=page)
#         df = df.append(pd.read_html(pg_url, header=0)[0], ignore_index=True)
#
#     # df.dropna()를 이용해 결측값 있는 행 제거
#     df = df.dropna()
#     # 상위 5개 데이터 확인하기
#     print(df.head())
#
#
#
