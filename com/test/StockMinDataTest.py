import matplotlib.pyplot as plt
import matplotlib.dates as md
import numpy as np
import datetime as dt
import time,datetime
import collections
import com.datautil.StockMinData as smd
import operator
__author__ = 'Zhenxin Lei'

duration=60*30
high,low=smd.StockMinData('JPM','20141006-20141017').historicalHighAndLow(duration)

#plot high close price
high=sorted(high.items(), key=operator.itemgetter(0))
x=[]
y=[]
for  highPrice in high:
    # x.append(datetime.datetime.fromtimestamp(
    #             highPrice[0]
    #             ).strftime('%Y-%m-%d %H:%M:%S')
    #         )
    x.append(highPrice[0])
    y.append(highPrice[1])
plt.plot(x,y,label="high price")

#plot low high price
y=[]
x=[]
low=sorted(low.items(), key=operator.itemgetter(0))
for  highPrice in low:
    # x.append(datetime.datetime.fromtimestamp(
    #             highPrice[0]
    #             ).strftime('%Y-%m-%d %H:%M:%S')
    #         )
    x.append(highPrice[0])
    y.append(highPrice[1])
plt.plot(x,y,label="low price")

#plot avg price
y=[]
fiboRet=[[],[],[]] #fibonacci 38.2%,50%, 61.8%
for  i in range(0,len(high)):
    avg=(high[i][1]+low[i][1])/2
    fibo_382=(high[i][1]-low[i][1])*0.382+low[i][1]
    fibo_618=(high[i][1]-low[i][1])*0.618+low[i][1]
    fiboRet[0].append(fibo_382)
    fiboRet[2].append(fibo_618)
    fiboRet[1].append(avg)
    #y.append(avg)
#plt.plot(x,y,'y', label="avg price")
plt.plot(x,fiboRet[0],label="Finbo-38.2%")
plt.plot(x,fiboRet[1],label="Finbo-50%")
plt.plot(x,fiboRet[2],label="Finbo-61.8%")

# add closed price to plot
stockData=smd.StockMinData('JPM','20141006-20141017').stockData
stockData=sorted(stockData.items(),key=operator.itemgetter(0))

i=0
while (high[0][0]>stockData[i][0]):
    i+=1

stockData=stockData[i:]
y=[]
for  highPrice in stockData:
    y.append(highPrice[1][0])
plt.plot(x,y, label="close price")

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.title("JPM 20141006-20141017")
plt.show()

