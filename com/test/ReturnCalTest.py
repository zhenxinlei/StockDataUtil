__author__ = 'Zhenxin Lei'

import pandas.io.data as pdata
import pandas
import  numpy as np

import com.datautil.ReturnCal.Implement.EqReCalImp as reCal
import com.datautil.RiskCal.EqCVarCalImp as cVarCal
from com.datautil.RankingEng import StockRankingEng


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
"A","AA","AAPL","ABBV","ABC","ABT","ACE","ACN","ACT","ADBE","ADI","ADM","ADP","ADS","ADSK","ADT","AEE",
"AEP","AES","AET","AFL","AGN","AIG","AIV","AIZ","AKAM","ALL","ALLE","ALTR","ALXN","AMAT","AME","AMG",
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
"HCN","HCP","HD","HES","HIG","HOG","HON","HOT","HP","HPQ","HRB","HRL","HRS","HSP","HST","HSY",
"HUM","IBM","ICE","IFF","INTC","INTU","IP","IPG","IR","IRM","ISRG","ITW","IVZ","JCI","JEC","JNJ",
"JNPR","JOY","JPM","JWN","K","KEY","KIM","KLAC","KMB","KMI","KMX","KO","KORS","KR","KRFT","KSS",
"KSU","L","LB","LEG","LEN","LH","LLL","LLTC","LLY","LM","LMT","LNC","LO","LOW","LRCX","LUK","LUV",
"LVLT","LYB","M","MA","MAC","MAR","MAS","MAT","MCD","MCHP","MCK","MCO","MDLZ","MDT","MET","MHFI","MHK",
"MJN","MKC","MLM","MMC","MMM","MNK","MNST","MO","MON","MOS","MPC","MRK","MRO","MS","MSFT","MSI","MTB","MU","MUR",
"MWV","MYL","NAVI","NBL","NBR","NDAQ","NE","NEE","NEM","NFLX","NFX","NI","NKE","NLSN","NOC","NOV","NRG","NSC","NTAP",
"NTRS","NU","NUE","NVDA","NWL","NWSA","OI","OKE","OMC","ORCL","ORLY","OXY","PAYX","PBCT","PBI","PCAR","PCG","PCL",
"PCLN","PCP","PDCO","PEG","PEP","PETM","PFE","PFG","PG","PGR","PH","PHM","PKI","PLD","PLL","PM","PNC","PNR","PNW",
"POM","PPG","PPL","PRGO","PRU","PSA","PSX","PVH","PWR","PX","PXD","QCOM","QEP","R","RAI","RCL","REGN","RF","RHI",
"RHT","RIG","RL","ROK","ROP","ROST","RRC","RSG","RTN","SBUX","SCG","SCHW","SE","SEE","SHW","SIAL","SJM","SLB",
"SNA","SNDK","SNI","SO","SPG","SPLS","SRCL","SRE","STI",
"STJ","STT","STX","STZ","SWK","SWN","SWY","SYK","SYMC","SYY","T","TAP","TDC","TE","TEG","TEL",
"TGT","THC","TIF","TJX","TMK","TMO","TRIP","TROW","TRV","TSCO","TSN","TSO","TSS","TWC","TWX","TXN",
"TXT","TYC","UA","UHS","UNH","UNM","UNP","UPS","URBN","URI","USB","UTX","V","VAR","VFC","VIAB","VLO","VMC","VNO","VRSN","VRTX","VTR","VZ","WAG",
"WAT","WDC","WEC","WFC","WFM","WHR","WIN","WM","WMB","WMT","WU","WY",
"WYN","WYNN","XEC","XEL","XL","XLNX","XOM","XRAY","XRX","XYL","YHOO","YUM","ZION","ZMH"
])


print (symbol)
stockprice = pdata.get_data_yahoo(symbol, "3/15/2014", "3/15/2015",3,0.001,True,True,25)
#print(stockprice.Close.values)
a=stockprice.Close.values[0][0]
[p,r,c]=stockprice.shape
samplePriceMx=stockprice.Close.values
returndate=stockprice.Close._stat_axis[1:]

#samplePriceMx=[[float('nan'), 3],[1,1],[2,2],[a,2],[a,2],[3,4]]
#eqRe=reCal.eqDailyReImp(samplePriceMx)
eqLogRe=reCal.eqLogReImp(samplePriceMx)


# priceDateDict=dict
# for i in range(len(returndate)):
#     priceDateDict.update({returndate[i],eqLogRe[i]})
logReDateMx = pandas.DataFrame(eqLogRe, returndate, symbol)

# can print stock symbol, but symbol has to be large enough 
StockRankingEng.momRanking(logReDateMx, 20, 5, 1)