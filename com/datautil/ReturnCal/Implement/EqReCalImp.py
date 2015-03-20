__author__ = 'Zhenxin Lei'
import pandas.io.data
import numpy as np


def eqDailyReImp(priceMx) -> np.ndarray :
    """
    Calculate equities matrix return( ordered from oldest date to latest date) with method:
    R_t= (P_t - P_{t-1})/ P_{t-1}
    :param priceMx: price matrix without symbol header
        price matrix [row][column]
        [row] stocks' price in same time
        [column] one stock price in different time
    :return: return Matrix with symbol at 1st row
    :rtype : numpy.ndarray
    """
    [r, c] = np.shape(priceMx)
    reMx = [[0 for x in range(c)] for x in range(r - 1)]
    for i in range(0, r - 1):

        reMx[i] = ((priceMx[i + 1] - priceMx[i]) / priceMx[i]).tolist()

    return np.core.multiarray.array(reMx)


def eqLogReImp(priceMx):
    """

    :param priceMx:
    :return: numpy.ndarray
    """
    [r, c] = np.shape(priceMx)
    reMx = [[0 for x in range(c)] for x in range(r - 1)]
    for i in range(r-1):
        reMx[i]=np.emath.log(priceMx[i+1]/priceMx[i])
    return  np.core.multiarray.array(reMx)

