import datetime
import re,json
import urllib.request, urllib.response, pandas.io.data


__author__ = 'Zhenxin Lei'

# http://www.google.com/finance/getprices?i=1&p=10d&f=d,o,h,l,c,v&df=cpct&q=JPM
# EXCHANGE%3DNYSE
# MARKET_OPEN_MINUTE=570
# MARKET_CLOSE_MINUTE=960
# INTERVAL=1
# COLUMNS=DATE,CLOSE,HIGH,LOW,OPEN,VOLUME
# DATA=
# TIMEZONE_OFFSET=-240
# a1414416660,58.525,58.54,58.45,58.45,268465
# 60,58.36,58.52,58.31,58.52,89760



class RealTimeData:
    symbol=""
    source=""
    path="http://www.google.com/finance/getprices?"
    interval=1 #seconds
    period=1 #days

    def getattr(self):
        return self.symbol,self.source,self.path

    def setattr(self):
        self.symbol="JPM"
        self.source="GOOGLE"
        self.path=""

    def setPath(self,interval,period,symbol):
        # self.path="http://www.google.com/finance/getprices?"+"i="+interval+"&p="+period+"d"\
        # +"&f=d,o,h,l,c,v&df=cpct&q="+symbol

        self.path='http://finance.google.com/finance/info?q=%s' %symbol

    def getRealTimeData(self):
        content=urllib.request.urlopen(self.path)
        obj=11
        print(obj)
        print(content)

rtd=RealTimeData
rtd.setPath(rtd,"1","1","JPM")
rtd.getRealTimeData(rtd)

list=['JPM']
print(pandas.io.data.get_data_yahoo(list[0],'9/1/2014','11/1/2014',3,0.001,False,False,25))
print(pandas.io.data.get_quote_yahoo(list[0]))
print(1414416660+960)

print(
    datetime.datetime.fromtimestamp(
        1414416660
    ).strftime('%Y-%m-%d %H:%M:%S')
)