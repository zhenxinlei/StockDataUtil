import com.datautil.StockMinData as StockMinData
import pandas.algos
import collections

__author__ = 'Zhenxin Lei'


class PlotStockPrice:
    stockData = dict()
    def __init__(self):
        stockData = dict()

    def plotStockPrice(self):
        #stockData= StockMinData.StockMinData().stockData
        print(stockData)

PlotStockPrice().plotStockPrice()
