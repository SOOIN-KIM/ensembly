import pandas as pd
import sqlite3
import pandas_datareader.data as web
import datetime
import timedelta
from ensembley.web_crawling.naver_web_crawling import code_hub


def code_ks(code_txt=pd.read_csv('kost_kost', sep=',', encoding='UTF-8')):
    code_1 = code_txt['0']
    code = code_1.tolist()
    return code



def code_yahoo(code):
    start = datetime.datetime(2011,1,1)
    end = datetime.datetime.today()
    # start = end - timedelta
    columnList = ['High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close', 'Code']
    stock = pd.DataFrame(columns=columnList)
    for c in code_ks():
        df = web.DataReader(c, 'yahoo', start, end)
        df['Code'] = c
        stock = pd.concat([stock, df])
        stock = stock.filter(columnList)
        con = sqlite3.connect('stock_10.db')
        stock.to_sql('stock_10', con, if_exists='replace')

        read_df = pd.read_sql("select * from 'stock_10'", con)
        print(read_df.head())
        print(read_df.tail())
if __name__ == '__main__':
    # start = datetime.datetime(2020, 2, 1)
    # end = datetime.date.today() - datetime.timedelta(1)
    # columnList = ['High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close', 'Code']
    # stock = pd.DataFrame(columns = columnList)
    # for c in code_ks():
    #     df = web.DataReader(c, 'yahoo', start, end)
    #     df['Code'] = c
    #     stock = pd.concat([stock,df])
    #     stock = stock.filter(columnList)
    #
    # con = sqlite3.connect('stock.db')
    # stock.to_sql('stock', con, if_exists='replace')
    #
    # read_df = pd.read_sql("select * from 'stock'", con)
    # print(read_df)

    code_yahoo(code_ks())
