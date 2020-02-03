import requests
import traceback
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup


# 현재코드 가져오는 함수
# company_code를 입력받아 bs_obj를 출력
def get_bs_obj(company_code):
    url = "https://finance.naver.com/item/main.nhn?code=" + company_code
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj

# 현재코드 가져오는 함수(get_bs_obj)를 받아 현재주식가격 리턴 하는 함수
# company_code를 입력받아 now_price를 출력
def get_price(company_code):
    bs_obj = get_bs_obj(company_code)
    no_today = bs_obj.find('p', {'class': 'no_today'})
    blind = no_today.find('span', {'class': 'blind'})
    now_price = blind.text
    return now_price

# 코드를 가져오는 함수를 입력받아서 오늘날짜 가격 기준 [시가,고가,저가,종가] 리
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

def stock_price(codes, page_num =1):

    for code in codes:
        print(code)
        result = [[], [], [], [], [], [], []]
        for n in range(page_num):
            url = 'https://finance.naver.com/item/sise_day.nhn?code='+code+'&page='+str(n+1)
            r = requests.get(url)
            html = r.content
            soup = BeautifulSoup(html, 'html.parser')
            tr = soup.select('table > tr')

            for i in range(1, len(tr)-1):
                if tr[i].select('td')[0].text.strip():
                    result[0].append(tr[i].select('td')[0].text.strip())
                    result[1].append(tr[i].select('td')[1].text.strip())
                    result[2].append(tr[i].select('td')[2].text.strip())
                    result[3].append(tr[i].select('td')[3].text.strip())
                    result[4].append(tr[i].select('td')[4].text.strip())
                    result[5].append(tr[i].select('td')[5].text.strip())
                    result[6].append(tr[i].select('td')[6].text.strip())

        for i in range(len(result[0])):
            print(result[0][i], result[1][i], result[2][i], result[3][i],result[4][i],result[5][i], result[6][i])


def get_finance(company_code):
    bs_obj = get_bs_obj(company_code)

    finance_html = bs_obj.select('div.section.cop_analysis div.sub_section')[0]
    th_data = [item.get_text().strip() for item in finance_html.select('thead th')]
    annual_date = th_data[3:7]
    quarter_date = th_data[7:13]

    finance_index = [item.get_text().strip() for item in finance_html.select('th.h_th2')][3:]
    finance_data = [item.get_text().strip() for item in finance_html.select('td')]

    finance_data = np.array(finance_data)
    finance_data.resize(len(finance_index),10)
    finance_date = annual_date + quarter_date

    finance = pd.DataFrame(data = finance_data[0:,0:], index=finance_index,columns=finance_date)

    return(finance.T)

def code_hub(code_txt=pd.read_csv('kosp_list', sep=',', encoding='UTF-8')):
    code_1 = code_txt['0']
    code_2= code_1.tolist()
    # codes = [code for code in code_2]
    return code_2

# def daily_stock_price(code):




if __name__ == '__main__':
    stock_price(code_hub())







