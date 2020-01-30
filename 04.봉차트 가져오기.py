import requests
from bs4 import BeautifulSoup

def get_bs_obj(company_code):
    url = "https://finance.naver.com/item/main.nhn?code=" + company_code
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj

def get_candle_chart(company_code):
    bs_obj = get_bs_obj(company_code)

    # close 종가(전일)
    td_first = bs_obj.find('td', {'class': 'first'})
    blind = td_first.find('span', {'class' : 'blind'})
    close = blind.text

    # high 고가
    table =bs_obj.find('table',{'class','no_info'}) #태그 table, 속성값 no_info 찾기
    trs = table.find_all('tr') # tr을 list로 []
    first_tr = trs[0] # 첫 번째 tr 지정
    tds = first_tr.find_all('td')
    second_tds = tds[1] # 두 번째 td 지정
    high = second_tds.find('span',{'class' : 'blind'}).text

    # open 시가
    second_tr = trs[1]  # 두 번째 tr 지정
    tds_second_tr = second_tr.find_all('td')  # 두 번째 tr 안에서 td를 list로
    first_td_in_second_tr = tds_second_tr[0]  # 첫 번째 td 지정
    open = first_td_in_second_tr.find('span', {'class': 'blind'}).text

    # low 저가
    second_td_in_second_tr = tds_second_tr[1] # 두 번째 td 지정
    low = second_td_in_second_tr.find('span', {'class':'blind'}).text

    return {'close': close, 'high':high, 'open':open, 'low':low}

if __name__ == '__main__':
    company_codes = ['005930','068270']

    for item in company_codes:
        candle_chart = get_candle_chart(item)
        print(candle_chart)





























