__author__ = 'Zhenxin Lei'
import numpy as np

def eqCVarCalImp(reMx, alpha):
    """
    Historical conditional VAR
    :param reMx: ndarray
    :param alpha:
    """
    [r,c]=np.shape(reMx)
    cVar=[0 for i in range(c)]


    # sort return matrix for each column
    for i in range(c):
        reMx[:,i]=sorted(reMx[:,i])

    varMx=reMx[0:int(r*alpha),0:4]

    print(varMx)
    return np.core.multiarray.array(np.asmatrix(varMx).mean(0))

