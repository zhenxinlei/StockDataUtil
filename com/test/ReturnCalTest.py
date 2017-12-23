__author__ = 'Zhenxin Lei'

#import pandas.io.data as pdata
from pandas_datareader import data as pdata
import pandas
import  numpy as np

import com.datautil.ReturnCal.Implement.EqReCalImp as reCal
import com.datautil.RiskCal.EqCVarCalImp as cVarCal
from com.datautil.RankingEng import StockRankingEng
import com.datautil.SymbolList as symb

import fix_yahoo_finance as yf
yf.pdr_override() # <== that's all it takes :-)

r=10
c=5
#samplePriceMx=[ [0 for x in range(r)] for x in range(c)]

# 
# symbol=sorted(["JPM", "JMEI", "TSLA", "WMT"])
# 
# stockprice=pdata.get_data_yahoo(symbol,"11/1/2014","12/19/2014")
# #print(stockprice.Close.values)
# a=stockprice.Close.values[0][0]
# [p,r,c]=stockprice.shape
# samplePriceMx=stockprice.Close.values
# returndate=stockprice.Close._stat_axis[1:]
# 
# #samplePriceMx=[[float('nan'), 3],[1,1],[2,2],[a,2],[a,2],[3,4]]
# #eqRe=reCal.eqDailyReImp(samplePriceMx)
# eqLogRe=reCal.eqLogReImp(samplePriceMx)
# 
# 
# # priceDateDict=dict
# # for i in range(len(returndate)):
# #     priceDateDict.update({returndate[i],eqLogRe[i]})
# priceDateMx=pandas.DataFrame(eqLogRe,returndate,symbol)
# print(priceDateMx)
# 
# # to do list: implement momRanking()
# StockRankingEng.momRanking(priceDateMx,90,5,10 )
# 
# 
# 
# cVar=cVarCal.eqCVarCalImp(eqLogRe,0.05)
# 
# a=StockRankingEng.rankReOverCvar(eqLogRe,cVar)
# 
# #print(eqRe)
# 
# print (a)



symbol=sorted([
"A","AA","AAPL","ABBV","ABC","ABT","CB","ACN","ACT","ADBE","ADI","ADM","ADP","ADS","ADSK","ADT","AEE",
"AEP","AES","AET","AFL","AGN","AIG","AIV","AIZ","AKAM","ALL","ALLE","ALXN","AMAT","AME","AMG",
"AMGN","AMP","AMT","AMZN","AN","ANTM","AON","APA","APC","APD","APH","ARG","ATI","AVB","AVGO","AVP",
"AVY","AXP","AZO","BA","BAC","BAX","BBBY","BBT","BBY","BCR","BDX","BEN",
"BF.B","BHI","BIIB","BK","BLK","BLL","BMY","BRCM","BRK.B","BSX","BWA","BXP","C","CA","CAG","CAH",
"CAM","CAT","CB","CBG","CBS","CCE","CCI","CCL","CELG","CERN","CF","CFN",
"CHK","CHRW","CI","CINF","CL","CLX","CMA","CMCSA","CME","CMG","CMI",
"CMS","CNP","CNX","COF","COG","COH","COL","COP","COST","COV","CPB","CRM",
"CSC","CSCO","CSX","CTAS","CTL","CTSH","CTXS","CVC","CVS","CVX","D","DAL","DD","DE","DFS","DG",
"DGX","DHI","DHR","DIS","DISCA","DISCK","DLPH","DLTR","DNB","DNR",
"DO","DOV","DOW","DPS","DRI","DTE","DTV","DUK","DVA","DVN","EA","EBAY","ECL","ED","EFX","EIX",
"EL","EMC","EMN","EMR","EOG","EQR","EQT","ESRX","ESS","ESV","ETFC","ETN","ETR","EW",
"EXC","EXPD","EXPE","F","FAST","FB","FCX","FDO","FDX","FE","FFIV","FIS","FISV","FITB","FLIR","FLR",
"FLS","FMC","FOSL","FOXA","FSLR","FTI","FTR","GAS","GCI","GD","GE","GGP","GILD","GIS","GLW","GM",
"GMCR","GME","GNW","GOOG","GOOGL","GPC","GPS","GRMN","GS","GT","GWW","HAL","HAR","HAS","HBAN","HCBK",
"HCN","HCP","HD","HES","HIG","HOG","HON","HOT","HP","HPQ","HRB","HRL","HRS","HST","HSY",
"HUM","IBM","ICE","IFF","INTC","INTU","IP","IPG","IR","IRM","ISRG","ITW","IVZ","JCI","JEC","JNJ",
"JNPR","JOY","JPM","JWN","K","KEY","KIM","KLAC","KMB","KMI","KMX","KO","KORS","KR","KSS",
"KSU","L","LB","LEG","LEN","LH","LLL","LLTC","LLY","LM","LMT","LNC","LOW","LRCX","LUK","LUV",
"LVLT","LYB","M","MA","MAC","MAR","MAS","MAT","MCD","MCHP","MCK","MCO","MDLZ","MDT","MET","MHK",
"MJN","MKC","MLM","MMC","MMM","MNK","MNST","MO","MON","MOS","MPC","MRK","MRO","MS","MSFT","MSI","MTB","MU","MUR",
"MWV","MYL","NAVI","NBL","NBR","NDAQ","NE","NEE","NEM","NFLX","NFX","NI","NKE","NLSN","NOC","NOV","NRG","NSC","NTAP",
"NTRS","NU","NUE","NVDA","NWL","NWSA","OI","OKE","OMC","ORCL","ORLY","OXY","PAYX","PBCT","PBI","PCAR","PCG","PCL",
"PCLN","PCP","PDCO","PEG","PEP","PETM","PFE","PFG","PG","PGR","PH","PHM","PKI","PLD","PLL","PM","PNC","PNR","PNW",
"PPG","PPL","PRGO","PRU","PSA","PSX","PVH","PWR","PX","PXD","QCOM","QEP","R","RAI","RCL","REGN","RF","RHI",
"RHT","RIG","RL","ROK","ROP","ROST","RRC","RSG","RTN","SBUX","SCG","SCHW","SE","SEE","SHW","SJM","SLB",
"SNA","SNDK","SNI","SO","SPG","SPLS","SRCL","SRE","STI",
"STJ","STT","STX","STZ","SWK","SWN","SWY","SYK","SYMC","SYY","T","TAP","TDC","TE","TEG","TEL",
"TGT","THC","TIF","TJX","TMK","TMO","TRIP","TROW","TRV","TSCO","TSN","TSO","TSS","TWC","TWX","TXN",
"TXT","TYC","UA","UHS","UNH","UNM","UNP","UPS","URBN","URI","USB","UTX","V","VAR","VFC","VIAB","VLO","VMC","VNO","VRSN","VRTX","VTR","VZ","WAG",
"WAT","WDC","WEC","WFC","WFM","WHR","WIN","WM","WMB","WMT","WU","WY",
"WYN","WYNN","XEC","XEL","XL","XLNX","XOM","XRAY","XRX","XYL","YHOO","YUM","ZION","ZMH"
])

# new pandas api
#symbol=symb.get_ticker_array_by_country("USA")

symbol = sorted([
    'ABT', 'ABBV', 'ACN', 'CB', 'ADBE', 'ADT', 'AAP', 'AES', 'AET', 'AFL', 'AMG', 'A', 'APD', 'ARG', 'AKAM',
     'AA', 'AGN', 'ALXN', 'ALLE', 'ADS', 'ALL', 'MO', 'AMZN', 'AEE', 'AAL', 'AEP', 'AXP', 'AIG', 'AMT', 'AMP',
     'ABC', 'AME', 'AMGN', 'APH', 'APC', 'ADI', 'AON', 'APA', 'AIV', 'AMAT', 'ADM', 'AIZ', 'T', 'ADSK', 'ADP', 'AN', 'AZO',
     'AVGO', 'AVB', 'AVY', 'BHI', 'BLL', 'BAC', 'BK', 'BCR', 'BXLT', 'BAX', 'BBT', 'BDX', 'BBBY', 'BRK-B', 'BBY', 'BLX',
       'HRB', 'BA', 'BWA', 'BXP', 'BSK.V', 'BMY', 'BF-B', 'CHRW', 'CA', 'CVC', 'COG', 'CPB', 'COF', 'CAH',
       'HSIC', 'KMX', 'CCL', 'CAT', 'CBG', 'CBS', 'CELG', 'CNP', 'CTL', 'CERN', 'CF', 'SCHW', 'CHK', 'CVX', 'CMG', 'CB',
       'CI', 'XEC', 'CINF', 'CTAS', 'CSCO', 'C', 'CTXS', 'CLX', 'CME', 'CMS', 'COH', 'KO', 'CCE', 'CTSH', 'CL', 'CMCSA',
       'CMA', 'CSC', 'CAG', 'COP', 'CNX', 'ED', 'STZ', 'GLW', 'COST', 'CCI', 'CSX', 'CMI', 'CVS', 'DHI', 'DHR', 'DRI', 'DVA',
       'DE', 'DLPH', 'DAL', 'XRAY', 'DVN', 'DO', 'DFS', 'DISCA', 'DISCK', 'DG', 'DLTR', 'D', 'DOV', 'DOW', 'DPS', 'DTE',
       'DD', 'DUK', 'DNB', 'ETFC', 'EMN', 'ETN', 'EBAY', 'ECL', 'EIX', 'EW', 'EA', 'EMC', 'EMR', 'ENDP', 'ESV', 'ETR', 'EOG', 'EQT',
       'EFX', 'EQIX', 'EQR', 'ESS', 'EL', 'ES', 'EXC', 'EXPE', 'EXPD', 'ESRX', 'XOM', 'FFIV', 'FB', 'FAST', 'FDX', 'FIS', 'FITB',
       'FSLR', 'FE', 'FLIR', 'FLS', 'FLR', 'FMC', 'FTI', 'F', 'FOSL', 'BEN', 'FCX', 'FTR', 'GME', 'GPS', 'GRMN', 'GD',
       'GE', 'GGP', 'GIS', 'GM', 'GPC', 'GNW', 'GILD', 'GS', 'GT', 'GOOGL', 'GOOG', 'GWW', 'HAL', 'HBI', 'HOG', 'HAR', 'HRS',
       'HIG', 'HAS', 'HCA', 'HCP', 'HCN', 'HP', 'HES', 'HPQ', 'HD', 'HON', 'HRL', 'HST', 'HUM', 'HBAN', 'ITW',
       'IR', 'INTC', 'ICE', 'IBM', 'IP', 'IPG', 'IFF', 'INTU', 'ISRG', 'IVZ', 'IRM', 'JEC', 'JBHT', 'JNJ', 'JCI', 'JOY', 'JPM',
       'JNPR', 'KSU', 'K', 'KEY', 'KMB', 'KIM', 'KMI', 'KLAC', 'KSS', 'KHC', 'KR', 'LB', 'LLL', 'LH', 'LRCX', 'LM',
       'LEG', 'LEN', 'LVLT', 'LUK', 'LLY', 'LNC', 'LLTC', 'LMT', 'L', 'LOW', 'LYB', 'MTB', 'MAC', 'M', 'MNK', 'MRO', 'MPC', 'MAR',
       'MMC', 'MLM', 'MAS', 'MA', 'MAT', 'MKC', 'MCD', 'SPGI', 'MCK', 'MJN', 'MMV', 'MDT', 'MRK', 'MET', 'KORS', 'MCHP', 'MU', 'MSFT',
       'MHK', 'TAP', 'MDLZ', 'MON', 'MNST', 'MCO', 'MS', 'MOS', 'MSI', 'MUR', 'MYL', 'NDAQ', 'NOV', 'NAVI', 'NTAP', 'NFLX', 'NWL', 'NFX',
       'NEM', 'NWSA', 'NEE', 'NLSN', 'NKE', 'NI', 'NE', 'NBL', 'JWN', 'NSC', 'NTRS', 'NOC', 'NRG', 'NUE', 'NVDA', 'ORLY', 'OXY', 'OMC', 'OKE',
       'ORCL', 'OI', 'PCAR', 'PH', 'PDCO', 'PAYX', 'PNR', 'PBCT', 'PEP', 'PKI', 'PRGO', 'PFE', 'PCG', 'PM', 'PSX', 'PNW', 'PXD',
       'PBI', 'PNC', 'RL', 'PPG', 'PPL', 'PX', 'PCLN', 'PFG', 'PG', 'PGR', 'PLD', 'PRU', 'PEG', 'PSA', 'PHM', 'PVH', 'QRVO', 'PWR',
       'QCOM', 'DGX', 'RRC', 'RTN', 'O', 'RHT', 'REGN', 'RF', 'RSG', 'RAI', 'RHI', 'ROK', 'COL', 'ROP', 'ROST', 'R', 'CRM', 'SNDK', 'SCG',
       'SLB', 'SNI', 'STX', 'SEE', 'SRE', 'SHW', 'SPG', 'SWKS', 'SLG', 'SJM', 'SNA', 'SO', 'LUV', 'SWN', 'SE', 'STJ', 'SWK', 'SPLS',
       'SBUX', 'HOT', 'STT', 'SRCL', 'SYK', 'STI', 'SYMC', 'SYY', 'TROW', 'TGT', 'TEL', 'TGNA', 'THC', 'TDC', 'TSO', 'TXN', 'TXT', 'HSY',
       'TRV', 'TMO', 'TIF', 'TWX', 'TWX', 'TMK', 'TSS', 'TSCO', 'RIG', 'TRIP', 'FOXA', 'TSN', 'TYC', 'UA', 'UNP', 'UNH', 'UPS', 'URI',
       'UTX', 'UHS', 'UNM', 'URBN', 'VFC', 'VLO', 'VAR', 'VTR', 'VRSN', 'VZ', 'VRTX', 'VIAB', 'V', 'VNO', 'VMC', 'WMT', 'WBA', 'DIS', 'WM', 'WAT',
       'ANTM', 'WFC', 'WDC', 'WU', 'WY', 'WHR', 'WFM', 'WMB', 'WEC', 'WYN', 'WYNN', 'XEL', 'XRX', 'XLNX', 'XL', 'XYL', 'YHOO', 'YUM', 'ZBH', 'ZION', 'ZTS',

        'TSLA','AMD', 'MU','NVDA',
                 ])

print(len(symbol))

stockprice = pdata.get_data_yahoo(symbol, "2016-1-1", "2017-7-1")
print(len(symbol))
print(stockprice.shape)
#print(stockprice)

#stockprice = pdata.get_data_yahoo(symbol, "1/1/2015", "8/7/2016",3,0.001,True,True,25)
#print(stockprice.Close.values)
a=stockprice.Close.values[0][0]
[p,r,c]=stockprice.shape
samplePriceMx=stockprice.Close.values
returndate=stockprice.Close._stat_axis[1:]
print(returndate.shape)

#samplePriceMx=[[float('nan'), 3],[1,1],[2,2],[a,2],[a,2],[3,4]]
#eqRe=reCal.eqDailyReImp(samplePriceMx)
eqLogRe=reCal.eqLogReImp(samplePriceMx)
print(eqLogRe.shape)


# priceDateDict=dict
# for i in range(len(returndate)):
#     priceDateDict.update({returndate[i],eqLogRe[i]})
logReDateMx = pandas.DataFrame(eqLogRe, returndate, stockprice.axes[2])

print("log return data matirx")

# can print stock symbol, but symbol has to be large enough 
StockRankingEng.momRanking(logReDateMx, 120, 60, 100)