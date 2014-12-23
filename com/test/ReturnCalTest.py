__author__ = 'Zhenxin Lei'

import pandas.io.data as pdata
import pandas
import  numpy as np

import com.datautil.ReturnCal.Implement.EqReCalImp as reCal
import com.datautil.RiskCal.EqCVarCalImp as cVarCal
from com.datautil.RankingEng import StockRankingEng


r=10
c=5
#samplePriceMx=[ [0 for x in range(r)] for x in range(c)]


symbol=sorted(["JPM", "JMEI", "TSLA", "WMT"])

stockprice=pdata.get_data_yahoo(symbol,"11/1/2014","12/19/2014")
#print(stockprice.Close.values)
a=stockprice.Close.values[0][0]
[p,r,c]=stockprice.shape
samplePriceMx=stockprice.Close.values
returndate=stockprice.Close._stat_axis[1:]

#samplePriceMx=[[float('nan'), 3],[1,1],[2,2],[a,2],[a,2],[3,4]]
#eqRe=reCal.eqDailyReImp(samplePriceMx)
eqLogRe=reCal.eqLogReImp(samplePriceMx)


# priceDateDict=dict
# for i in range(len(returndate)):
#     priceDateDict.update({returndate[i],eqLogRe[i]})
priceDateMx=pandas.DataFrame(eqLogRe,returndate,symbol)
print(priceDateMx)

# to do list: implement momRanking()
StockRankingEng.momRanking(priceDateMx,90,5,10 )



cVar=cVarCal.eqCVarCalImp(eqLogRe,0.05)

a=StockRankingEng.rankReOverCvar(eqLogRe,cVar)

#print(eqRe)

print (a)