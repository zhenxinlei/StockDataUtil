__author__ = 'Zhenxin Lei'
import numpy as np
import pandas
import com.datautil.RiskCal.EqCVarCalImp as cVarCal

def rankReOverCvar(reMx, cvar ):
    '''

    :param reMx:
    :param cvar:
    :return:
        ranking result of stocks( column index)
    '''
    a=np.mean(reMx,0)/cvar
    
    array = np.array(a[0])
    for i in range(len(array)):
       

        if np.isnan(array[i]):
            
            array[i]=-float("inf")
    order = array.argsort()
    ranks = order.argsort()

    return ranks

def momRanking(reData, rankPers, holdPers, topPercent):
    """
    :param data:
        asset retrun dataframe
    :param rankPers:
    :param holdPers:
    :param topPercent:
    :return:
    """
    
    eqRe = reData.values
    [r, c] = np.shape(eqRe)
    date = []
    symbol = []
    alpha =0.06

    i = 0
    while i + rankPers - 1 <= r - 1:
        subperiod = eqRe[i:i + rankPers - 1, :]
        cVar = cVarCal.eqCVarCalImp(subperiod, alpha)
        ranking = rankReOverCvar(subperiod, cVar)
        symbolindex = np.argsort(ranking)[::-1]
        
        
        symbolindex = symbolindex[:int(len(ranking) * topPercent / 100)]
        
        # date.append(i + rankPers)
        date.append(reData.index[i + rankPers])
        a=reData.axes[1][symbolindex]
       
        symbol.append(reData.axes[1][symbolindex])
        # date=date.append([reData.axes[0][i]])
        #symbol=symbol.append(reData.axes[1][symbolindex])
        if i+holdPers+rankPers>r-1:
            break
        i = i + holdPers

    rankindex = [i + 1 for i in range(int(c * topPercent / 100))]
    recomStkData = pandas.DataFrame(symbol, date, rankindex)
    print(recomStkData)

    return recomStkData

   