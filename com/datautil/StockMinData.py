import csv, string, sys, datetime, collections
import _datetime, string


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
    fileTimPeriod='20141006-20141017'
    #

    def __init__(self,ticker,fileTimPeriod):
        self.ticker=ticker
        self.fileTimPeriod=fileTimPeriod
        self.readMinData()

    def readMinData(self):
        csvFile=open(self.filePath+self.ticker+' '+self.fileTimPeriod+self.fileType)
        reader =csv.reader(csvFile, delimiter=',')
        for row in reader:
           # self.stockData.update(row[1]: row[2:])
            self.timeStamp.append(int(row[0]))
            self.stockData.update({row[0]:row[1:]})

        return self.stockData

    # duration unit is second, 1min=60s
    def historicalHighAndLow(self,duration):
        high=dict()
        low=dict()
        startTime=self.timeStamp[0]

        #get first 5 min highest and lowest
        localMax=float(self.stockData[str(startTime)][0])
        localMin=float(self.stockData[str(startTime)][0])
        startDurationTime=0

        for i in self.timeStamp:
            print(self.stockData[str(i)])
            print(self.stockData[str(i)][0])
            print(float(self.stockData[str(i)][0]))
            if (i>(startTime+duration)):
                startDurationTime=i
                break

        count=0
        for startTimeStamp in self.timeStamp[self.timeStamp.index(startDurationTime):]:
             endTimeStamp= self.timeStamp[self.timeStamp.index(startDurationTime)+count]

            def findMaxAndMin(self,startTimeStamp,endTimeStamp):
                localMax=float(self.stockData[str(startTimeStamp)][0])
                localMin=float(self.stockData[str(endTimeStamp)][0])

                startIndex=self.timeStamp.index[startTimeStamp]
                endIndex=self.timeStamp.index[endTimeStamp]
                for i in self.timeStamp[startIndex:endIndex]:
                    if (float(self.stockData[str(i)][0])>=float(localMax)):
                        localMax=float(self.stockData[str(i)][0])
                    if (float(self.stockData[str(i)][0])<=float(localMin)):
                        localMin=float(self.stockData[str(i)][0])

                return localMax, localMin

            high.update({startDurationTime:localMax})
            low.update({startDurationTime:localMin})
            count++

        for i in self.timeStamp:
            print(
            datetime.datetime.fromtimestamp(
                i
                ).strftime('%Y-%m-%d %H:%M:%S')
            )


        return high,low


print(StockMinData('JPM','20141006-20141017').historicalHighAndLow(1500))


