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
    


def L11(X,alpha):
    """ Function that takes a vector X and a smoothing parameter alpha and return the smoothL1-SC L1-norm and its gradient  """
    l1 = 1/alpha(np.log(1+ np.exp(alpha*X)) + np.log(1+ np.exp(-alpha*X)))
    grad = (np.exp(alpha*X)- np.exp(-alpha*X))/((1+np.exp(alpha*X))*(1+np.exp(-alpha*X)))
    return np.sum(l1), grad

def L222(X):
    """"Return the L2  norm squared and its gradiant, of the vector X """
    l2 = np.linalg.norm(X)**2
    grad = 2 * X
    return l2, grad

def L22(X):
    l2=np.linalg.norm(X)
    grad=X/l2;
    return l2, grad 

def L2g(X,group):
    Xg=np.zeros(len(X))
    for i in group :
        Xg[i]=X[i]
    return L2(Xg)
    

def PGL(X,lambdaGL,groups):
    """Return the Group LASSO penalisation
    Input :
        X: 1darray of betas 
        lambdaGL: strength of penalty
        groups : 2darray of int, matrix where 
        the i th row contains the indexes of the features in the group i"""
    l2=0
    grad=np.zeros(len(X))
    for i in range(np.shape(groups)[0]):
        l,g=L2g(X,groups[i])
        l2+=l;
        grad+=g;
    return lambdaGL*l2,lambdaGL*grad
        
    # result=0
    # for i in range(np.shape(groups)[0]):
    #     for j in range(np.shape(groups)[1]):
    #         Xg[i]+=X[groups[i][j]]**2
    #     Xg[i]=np.sqrt(Xg[i])
    # return lambdaGL*np.sum(Xg)

def LRG(X,groups,rivalgroup):
    group1=groups[rivalgroup[0]]
    group2=groups[rivalgroup[1]]
    l1,g1=L2g(X,group1)
    l2,g2=L2g(X,group2)
    l=l1*l2
    grad=g1*l2+l1*g1
    return l,grad


def PGR(X,lambdaGR,groups,rivalgroups):
    l2=0;
    grad=np.zeros(len(X))
    for i in range(np.shape(rivalgroups)[0]):
        l,g=LRG(X,groups,rivalgroups[i])
        l2+=l
        grad+=g
    return lambdaGR*l2,lambdaGR*grad
        
        
    
    




