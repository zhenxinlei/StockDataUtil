__author__ = 'Zhenxin Lei'
import numpy as np


def rankReOverCvar(reMx, cvar ):
    '''

    :param reMx:
    :param cvar:
    :return:
        ranking result of stocks( column index)
    '''
    a=np.mean(reMx,0)/cvar
    print(a)
    array = np.array(a[0])
    for i in range(len(array)):
        print(i)

        if np.isnan(array[i]):
            print(i)
            array[i]=-float("inf")
    order = array.argsort()
    ranks = order.argsort()

    return ranks

def momRanking(data, rankPers, holdPers, topPercent):
    """
    :param data:
        asset retrun dataframe
    :param rankPers:
    :param holdPers:
    :param topPercent:
    :return:
    """
    eqRe=data.values
    date=data._stat_axis


    return recomStkData