__author__ = 'Zhenxin Lei'

import pandas.io.data as pdata, pandas.io.excel as pexcel


# return symbol list
#{ {"Ticker":"YHOO","Name": "Yahoo! Inc.","Exch": "NMS","CatName": "S","Country":"USA","CatNum":"0"}

def get_yahoo_stock_tickers():
    excel=pexcel.read_excel('../../com/resource/Yahoo Ticker Symbols demo.xlsx','Stock',header=3,parse_cols='A:F')
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

#get_usa_yahoo_stock_tickers()