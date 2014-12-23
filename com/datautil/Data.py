import pandas
import math
__author__ = 'Zhenxin Lei'
import pandas.io.data as pdata
import com.datautil.SymbolList as slist
import pandas.io.excel as pexcel
import numpy as np

# Get High Low average price data of list of stocks
# return time, average price matrix
def get_avg_price_matrix(startDate,endDate):
    #symbolList=list(slist.get_usa_yahoo_stock_tickers().keys())
    symbolList=['RGDX', 'APC', 'FIGY', 'TIF', 'APB']
    d=pandas.DataFrame(columns=symbolList)
    for i in range(len(symbolList)):
        data=pdata.get_data_yahoo(symbolList[i],startDate,endDate)
        print(data.values)
        avg=(data.High+data.Low)/2
        #add avg serise to column
        d[symbolList[i]]=avg
        #print("+++++d.items+++++++++++++")
        #print(d.items)


    # print("+++++d.items+++++++++++++")
    # print(d.items)
    # #d.to_excel('../../com/resource/AvgHighLow.xlsx')
    #
    # print("d.value")
    # print(d.values)
    print("+++++d.keys+++++++++++++")
    print(d.keys())
    # print("+++++d.items+++++++++++++")
    # print(d.items)
    # print("+++++d.axes+++++++++++++")
    # print(d.axes)

    return d

def get_return(priceDataFrame):
    startDate='9/1/2014'
    endDate='11/7/2014'
    priceDataFrame=get_avg_price_matrix(startDate,endDate)
    d=priceDataFrame
    print(priceDataFrame.items)
    symbolList=['RGDX', 'APC', 'FIGY', 'TIF', 'APB']
    d=pandas.DataFrame(columns=symbolList)


    pre=priceDataFrame.values[0].copy()
    for i in range(1,len(priceDataFrame.values)):
        cur=priceDataFrame.values[i]
        temp=cur
        cur=np.log(cur/pre)
        pre=temp.copy()
        priceDataFrame.values[i]=cur
        b=priceDataFrame.values[i]
        #d.values[i]= priceDataFrame.values[i]/priceDataFrame.values[i-1]

        print('a====================')
        print(len(priceDataFrame.values))

    priceDataFrame.values[0]=np.zeros(len(priceDataFrame.keys()))
    priceDataFrame=priceDataFrame.values[1:]
    return priceDataFrame

startDate='9/1/2014'
endDate='11/7/2014'
d= get_avg_price_matrix(startDate,endDate)
print (get_return(d))

print('===============')
print ('data.row')
#print(data.values[0][0]) #get first column in first row in the dataframe


