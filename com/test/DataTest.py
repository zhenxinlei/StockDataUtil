__author__ = 'Zhenxin Lei'

import pandas
import pandas.io.data as pdata
import com.datautil.SymbolList as slist
import pandas.io.excel as pexcel
import numpy as np

startDate='9/1/2014'
endDate='11/7/2014'
symbolList=['RGDX', 'APC', 'FIGY', 'TIF', 'APB']
d=pandas.DataFrame(columns=symbolList)
for i in range(len(symbolList)):
    data=pdata.get_data_yahoo(symbolList[i],startDate,endDate)
    print(data.values)
    avg=(data.High+data.Low)/2

    #d=pandas.DataFrame(columns=symbolList)
    d[symbolList[i]]=avg
    print("+++++d.items+++++++++++++")
    print(d.items)

print("+++++d.items+++++++++++++")
print(d.items)


a=np.array([   0.8 ,   109.995  ,129.85 ,  102.13 ,   12.015])
b=np.array([   0.8  ,  112.075 , 130.7   , 101.445  , 11.985])
import math
c=np.log(a/b)
print (c)