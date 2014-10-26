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
plt.plot(x,y)

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
plt.plot(x,y)

#plot avg price
y=[]
for  i in range(0,len(high)):
    avg=(high[i][1]+low[i][1])/2
    y.append(avg)
plt.plot(x,y)


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
plt.plot(x,y)


plt.show()

