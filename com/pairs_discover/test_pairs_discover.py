
'''
this is test file for testing pairs_discover
'''

import numpy as np
import pandas as pd
from pandas_datareader import data as pdata
import matplotlib.pyplot as plt

import fix_yahoo_finance as yf
yf.pdr_override() # <== that's all it takes :-)


import time
from datetime import datetime
timestamp = int(time.mktime(datetime.now().timetuple()))


def findCorrParis(stocks, start_date, end_date, duration=120):
    try:

        s = datetime.strptime(start_date,'%Y-%m-%d')
        e = datetime.strptime(end_date,'%Y-%m-%d')
        if (e-s).days<duration:
            raise ArithmeticError
    except ArithmeticError:
        print("start date, end date is less than duration")

    raw_df = pdata.get_data_yahoo(stocks, start_date, end_date)

    closePx = raw_df["Close"]
    print("\n",closePx.iloc[0])

    rho =pd.rolling_corr(closePx,120)

    print(rho)



#def generateSignal(pairs):

symbol = sorted(["XLF","AMG","AFL","ALL","AXP","AIG","AMP","AON","AJG","AIZ","BAC","BK","BBT","BRK.B","BLK","HRB","BHF","COF","CBOE","SCHW","CB","CINF","C","CFG","CME","CMA","DFS","ETFC","RE","FITB","BEN","GS","HIG","HBAN","ICE","IVZ","JPM","KEY","LUK","LNC","L","MTB","MMC","MET","MCO","MS","NDAQ","NAVI","NTRS","PBCT","PNC","PFG","PGR","PRU","RJF","RF","SPGI","STT","STI","SYF","TROW","TMK","TRV","USB","UNM","WFC","WLTW","XL","ZION"])

#symbol =["ZION", "LNC","JPM"]
findCorrParis(symbol, "2017-01-01","2018-02-01")
