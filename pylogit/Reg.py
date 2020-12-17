# -*- coding: utf-8 -*-
from __future__ import absolute_import


import numpy as np

def L1(param,boxcox=False, get_grad=False):
    """
    Perform a LASSO (L1) regularization. 
    Input :
        - param : vector of parameter containing the betas and lambdas
        - boxcox : boolean which indicates if a boxcox transformation is 
                   realised over the data.
        - get_grad : boolean which indicates if the method must return the
                     regularisation or its gradient.
    Returns :
        if 'get_grad=False' : returns the value of the L1 regularisation over 
        the betas (the lambdas are not regularised thanks to boxcox input)
        if 'get_grad=True' : returns a 1D numpy array which is the gradient
                             vector of the regularisation.
    """
    if (boxcox):
        nlambda=int((len(param)-3)/2)
        param2=param[0:3+nlambda]
        X=np.array(param2)
    else :
        X=np.array(param)
    if get_grad:

        grad=np.copy(X)
        ind=np.where(X!=0)
        grad[ind]=np.sign(X[ind])
        if(boxcox):
            grad2=np.concatenate((grad, np.zeros(nlambda)))
            return grad2
        else :
            return grad #/np.linalg.norm(grad)
    else :
        return np.sum(np.abs(X))
    
    
def L2(param,boxcox=False, get_grad=False):
    """
    Perform a Ridge (L2) regularization. 
    Input :
        - param : vector of parameter containing the betas and lambdas
        - boxcox : boolean which indicates if a boxcox transformation is 
                   realised over the data.
        - get_grad : boolean which indicates if the method must return the
                     regularisation or its gradient.
    Returns :
        if 'get_grad=False' : returns the value of the L2 regularisation over 
        the betas (the lambdas are not regularised thanks to boxcox input)
        if 'get_grad=True' : returns a 1D numpy array which is the gradient
                             vector of the regularisation.
    """
    if (boxcox):
        nlambda=int((len(param)-3)/2)
        param2=param[0:3+nlambda]
        X=np.array(param2)
    else :
        X=np.array(param)
    if get_grad :
        if(boxcox):
            grad2=np.concatenate((2*X, np.zeros(nlambda)))
            return grad2
        else :
            return 2*X
    else :
        l2 = np.linalg.norm(X)**2
        grad = 2 * X
        return l2
    



    

