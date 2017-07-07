__author__ = 'Zhenxin Lei'

import pandas.io.excel as pexcel
from pandas_datareader import data as pdata
from datetime import datetime, timedelta



# return symbol list
#{ {"Ticker":"YHOO","Name": "Yahoo! Inc.","Exch": "NMS","CatName": "S","Country":"USA","CatNum":"0"}

def get_yahoo_stock_tickers():

    excel=pexcel.read_excel('../../com/resource/Yahoo Ticker Symbols - Jan 2016.xlsx','Stock',header=3,parse_cols='A:F')
    tickersDict=dict()
    for row in excel.values:
        if (not row[1]==""):
            tDist=dict()
            tDist.update({"Ticker":row[0],"Name":row[1],"Exch":row[2],"CatName":row[3],"Country":row[4],"CatNum":row[5]})
            tickersDict.update({row[0]:tDist})
    return tickersDict

#dic=get_yahoo_stock_tickers()
#print(dic.keys())

def get_usa_yahoo_stock_tickers():
    tickersDict=get_yahoo_stock_tickers()
    tDict=dict()
    for row in tickersDict.items():
        if("USA" in row[1].values()):
            tDict.update({row[0]:row[1]})
    return tDict

def get_ticker_array( ticker_dict):

    #print((ticker_dict.keys()))
    ticker_array = []
    for key, value in ticker_dict.items():
        # skip unavailable symbols
        try:
            pdata.get_data_yahoo(key,datetime.today() - timedelta(days=7), datetime.today())
        except Exception as inst:
            #print(inst)
            continue
        print(key)
        ticker_array.append(key)
    return sorted(ticker_array)

#get_usa_yahoo_stock_tickers()

def get_yahoo_stock_tickers_by_country(country):
    tickersDict=get_yahoo_stock_tickers()
    tDict=dict()
    for row in tickersDict.items():
        if(country in row[1].values()):
            tDict.update({row[0]:row[1]})
    return tDict

def get_ticker_array_by_country(country):
    ticker_dict = get_yahoo_stock_tickers_by_country(country)
    return get_ticker_array(ticker_dict)

#print(get_ticker_array_by_country("USA"))