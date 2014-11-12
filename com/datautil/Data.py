import pandas

__author__ = 'Zhenxin Lei'
import pandas.io.data as pdata
import com.datautil.SymbolList as slist

# Get High Low average price data of list of stocks
# return time, average price matrix
def get_avg_price_matrix(startDate,endDate):
    symbolList=list(slist.get_usa_yahoo_stock_tickers().keys())
    d=pandas.DataFrame()
    for i in range(len(symbolList)):
        data=pdata.get_data_yahoo(symbolList[i],startDate,endDate)
        avg=(data.High+data.Low)/2
        c={symbolList[i]:avg}
        d= d.append(c,ignore_index=True)

        #print(d.values)

    d
    print(d.APB.values)



startDate='9/1/2014'
endDate='11/7/2014'
#get_avg_price_matrix(startDate,endDate)
data=pdata.get_data_yahoo('JPM',startDate,endDate)
print ('data.keys')
print(data.keys())
print('===============')
print ('data.value')
print(data.values)
print('===============')
print ('data.row')
print(data.values[0][0]) #get first column in first row in the dataframe


