import csv, string, sys, datetime, collections
import _datetime, string
import os


__author__ = 'Zhenxin Lei'

class StockMinData:
    ticker='JPM'
    timeStamp=[]
    closePrice=0
    highPrice=0
    lowPrice=0
    openPrice=0
    volume=0
    stockData = dict()

    # file setup for temp
    fileType='.csv'
    filePath='E:/University/Trading/Data/'
    os.path.dirname(__file__)
    #fileTimPeriod='20141006-20141017'
    #

    def __init__(self,ticker,fileTimPeriod):
        self.ticker=ticker
        self.fileTimPeriod=fileTimPeriod
        self.readMinData()

    def readMinData(self):
        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path = "../../com/resource/"
        abs_file_path = os.path.join(script_dir,rel_path)
        csvFile=open(abs_file_path +self.ticker+' '+self.fileTimPeriod+self.fileType)
        #csvFile=open(self.filePath+self.ticker+' '+self.fileTimPeriod+self.fileType)
        reader =csv.reader(csvFile, delimiter=',')
        for row in reader:
           # self.stockData.update(row[1]: row[2:])
            self.timeStamp.append(int(row[0]))
            #self.stockData.update({row[0]:row[1:]})
            priceList=[]
            for i in row[1:]:
               priceList.append(float(i))
            self.stockData.update({int(row[0]):priceList})
        return self.stockData

    # duration unit is second, 1min=60s
    def historicalHighAndLow(self,duration):
        high=dict()
        low=dict()
        startTime=self.timeStamp[0]


        localMax=float(self.stockData[startTime][0])
        localMin=float(self.stockData[startTime][0])
        startDurationTime=0

        for i in self.timeStamp:
            if (i>(startTime+duration)):
                startDurationTime=i
                break

        offset=self.timeStamp.index(startDurationTime)-self.timeStamp.index(startTime)

        for endTimeStamp in self.timeStamp[self.timeStamp.index(startDurationTime):]:
            startTimeStamp= self.timeStamp[self.timeStamp.index(endTimeStamp)-offset]
            localMax,localMin=self.findMaxAndMin(startTimeStamp,endTimeStamp)
            high.update({endTimeStamp:localMax})
            low.update({endTimeStamp:localMin})

        # for i in self.timeStamp:
        #     print(
        #     datetime.datetime.fromtimestamp(
        #         i
        #         ).strftime('%Y-%m-%d %H:%M:%S')
        #     )
        return (high,low)

    def findMaxAndMin(self,startTimeStamp,endTimeStamp):
        _localMax=float(self.stockData[startTimeStamp][0])
        _localMin=float(self.stockData[startTimeStamp][0])

        startIndex=self.timeStamp.index(startTimeStamp)
        endIndex=self.timeStamp.index(endTimeStamp)
        for i in self.timeStamp[startIndex:endIndex+1]:
            if (float(self.stockData[i][0])>=float(_localMax)):
                _localMax=float(self.stockData[i][0])
            if (float(self.stockData[i][0])<=float(_localMin)):
                _localMin=float(self.stockData[i][0])
        return (_localMax, _localMin)


#print(StockMinData('JPM','20141006-20141017').historicalHighAndLow(1500))


