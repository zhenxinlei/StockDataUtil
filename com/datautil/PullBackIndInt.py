__author__ = 'Zhenxin Lei'

# ========================
# This is Pull Back Indicator interface.
# The icon for these alerts describes the chart of the corresponding stocks.
# Start with the stock's closing price from the previous day/hour/minute.  Follow the stock down to today's low.
# Report an alert when the stock returns 25% or 75% of the way from the low back to the close.
# A stock can report these alerts more than one time per day.
# http://www.trade-ideas.com/Help.html#PFL25C
# =======================

# ======================
# input StockMinData.stockData, threshold, type
# input [timeStamp1, open, close] [timeStamp2, open, close]
# output [timeStamp, [isPullBackFromHigh, is pullBackFromLow]]
#


class PullBackIndInt:
    pullBackThreshold=0.0
    pullBackFromType=('HIGH','LOW')


    def __init__(self,threshold,type):
        self.pullBackFromType=type
        self.pullBackThreshold=threshold

    def

    # return boolean isPullBackFromHigh
    def isPullBackFromHigh(self,previousClose,currentOpen, currentClose):
        if (previousClose<currentOpen):
            if(currentClose<currentOpen*self.pullBackThreshold):
                return True
        return  False

    # return boolean isPullBackFromLow
    def isPullBackFromLow(self,previousClose,currentOpen, currentClose):
        if (previousClose>currentOpen):
            if(currentClose>currentOpen*(1+self.pullBackThreshold)):
                return True
        return  False