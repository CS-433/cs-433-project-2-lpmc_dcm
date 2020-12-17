#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import OrderedDict
import pandas as pd
import numpy as np
import pylogit as pl
from sklearn import preprocessing
import scipy.io as sio
from tqdm import tqdm
import matplotlib
import matplotlib.pyplot as plt

"""
Files import from the project
"""
import helpers as helpers
import generate_long_data as gld


#%% 
"""
Generate the model. 
- Take 1/3 of the dataset of  observation. Therefore the regularisation
  performed over 26 320 observations. (call of 'generate_data()')
- These observations are then standardized according thanks to 'standardize()'
  method
- The model is constructed by calling 'create_choice_model' of pylogit which
  has as input :
      The dataset
      The definition of the utility realised by 'create_specification()'
      The model type, here 'MNL' for multinomial logit
"""

long_lpmc = gld.generate_data(train=True) # train=False for generating the test dataset
y = long_lpmc.copy()

# standardize what has to be standardized : custom_id, mode_id etc.. are ignored
y.iloc[:, 3::1] = helpers.standardize(long_lpmc.iloc[:, 3::1])


choice_column = "travel_mode"
obs_id_column = "custom_id"
custom_alt_id = "mode_id"
basic_specification = helpers.create_specification()

lpmc_mnltrain = pl.create_choice_model(data=y,
                                        alt_id_col=custom_alt_id,
                                        obs_id_col=obs_id_column,
                                        choice_col=choice_column,
                                        specification=basic_specification,
                                        model_type="MNL",
                                        names=None)

#%%
"""
Defines relevant parameter for the simulations.
Variables :
    num_simul= Number of desired simulation for the grid search of the 
               hyperparameter lambda_lasso, lambda_ridge or the two.
    num_points = For each regularisation of the grid search, defines the 
                 number of simulation realised by addind parameters.
    maxiter = Number of iterations realised by Scipy 'minimize()' to optimized
             the parameters.
    num_param_keep = vector of length num_points which indicates how many
                     parameters are kept to perform a simulation after 
                     regularization.
    init = Initial vector of parameters. Contains the 'ASC', the betas and 
           then the lambdas variables. ASC and betas are initialised to zero
           while the lambdas to 1.  
"""

num_simul=4
num_points=6
maxiter=50
num_param_keep=np.round(np.logspace(1,np.log10(240),num_points))
num_param_keep[0]=0
asc     = np.zeros(3)
beta    = np.zeros(240)
lmda    = np.ones(240)
init = np.concatenate((asc, beta, lmda))

"""
Lasso regularization. 
Variables :
    lasso = vector of length num_simul which contains the different values 
            of the hyperparameter lambda_lasso for the grid search.
    betasRl = 2D numpy array which stores the optimized paramters obtained
             with regularisation.
    likelihoodl = 2D numpy array of length (num_simul, num_points)
                For each lambda_lasso term, stores the likelihood obtained
                for each value of num_param_keep. 
    betaPl= Stores the optimized parameter for each simulation realised

"""
lasso=np.logspace(-1,0,num_simul);      
betasRl=np.ones((483,num_simul));
likelihoodl=np.ones((num_simul,num_points))
betaPl=np.ones((483,num_simul*num_points))


for j in tqdm(range(num_simul)):
        a = lpmc_mnltrain.fit_mle(init, maxiter=maxiter, lasso=lasso[j], boxcox=True, just_point=True) 
        betasRl[:,j] = a.x
        if (j==0):
            for k in tqdm(range(num_points)):
                index=helpers.generate_list(betasRl[:,j],int(num_param_keep[k]))
                b=lpmc_mnltrain.fit_mle(init, maxiter=maxiter, boxcox=True, reduced=True, indd=index, just_point=True)
                likelihoodl[j,k]=-1*b["fun"]
                betaPl[:,j*num_points+k]=b.x
        else:
            for k in tqdm(range(num_points-1)):
                index=helpers.generate_list(betasRl[:,j],int(num_param_keep[k]))
                b=lpmc_mnltrain.fit_mle(init, maxiter=maxiter, boxcox=True, reduced=True, indd=index, just_point=True)
                likelihoodl[j,k]=-1*b["fun"]
                betaPl[:,j*num_points+k]=b.x
            betaPl[:,j*num_points+(num_points-1)]= betaPl[:,num_points-1]
            likelihoodl[j,(num_points-1)]=likelihoodl[0,num_points-1]
            
"""
Ridge regularization. 
Variables :
    ridge = vector of length num_simul which contains the different values 
            of the hyperparameter lambda_ridge for the grid search.
    betasRr = 2D numpy array which stores the optimized paramters obtained
             with regularisation.
    likelihoodr = 2D numpy array of length (num_simul, num_points)
                For each lambda_lasso term, stores the likelihood obtained
                for each value of num_param_keep.
    betaPr= Stores the optimized parameter for each simulation realised

"""
ridge=np.logspace(-1,0,num_simul);      
betasRr=np.ones((483,num_simul));
likelihoodr=np.ones((num_simul,num_points))
betaPr=np.ones((483,num_simul*num_points))


for j in tqdm(range(num_simul)):
        a = lpmc_mnltrain.fit_mle(init, maxiter=maxiter, ridge=ridge[j], boxcox=True, just_point=True) 
        betasRr[:,j] = a.x
        if (j==0):
            for k in tqdm(range(num_points)):
                index=helpers.generate_list(betasRr[:,j],int(num_param_keep[k]))
                b=lpmc_mnltrain.fit_mle(init, maxiter=maxiter, boxcox=True, reduced=True, indd=index, just_point=True)
                likelihoodr[j,k]=-1*b["fun"]
                betaPr[:,j*num_points+k]=b.x
        else:
            for k in tqdm(range(num_points-1)):
                index=helpers.generate_list(betasRr[:,j],int(num_param_keep[k]))
                b=lpmc_mnltrain.fit_mle(init, maxiter=maxiter, boxcox=True, reduced=True, indd=index, just_point=True)
                likelihoodr[j,k]=-1*b["fun"]
                betaPr[:,j*num_points+k]=b.x
            betaPr[:,j*num_points+(num_points-1)]= betaPr[:,num_points-1]
            likelihoodr[j,(num_points-1)]=likelihoodr[0,num_points-1] 
            
"""
Ridge and lasso regularization. 
&
No regularization 
Variables :
    ridge = vector of length num_simul which contains the different values 
            of the hyperparameter lambda_ridge for the grid search.
    betasRr = 2D numpy array which stores the optimized paramters obtained
             with regularisation.
    likelihoodr = 2D numpy array of length (num_simul, num_points)
                For each lambda_lasso term, stores the likelihood obtained
                for each value of num_param_keep.
    betaPr= Stores the optimized parameter for each simulation realised

"""

num_ridge=4
num_lasso=2
num_points=6
maxiter=50

lassos=np.logspace(1,2,num_lasso)
ridges=np.logspace(-1,2,num_ridge)

betas_reg = np.ones((num_lasso, num_ridge, 483))
likelihoodlr = np.ones((num_lasso, num_ridge, num_points))
betas_sim = np.ones((num_lasso, num_ridge, num_points, 483))


for i in tqdm(range(num_lasso)):
    for j in tqdm(range(num_ridge)):
        
        tmp_reg = lpmc_mnltrain.fit_mle(init, maxiter=maxiter,ridge = lassos[i], ridge2=ridges[j], boxcox=True, just_point=True) 
        betas_reg[i,j,:] = tmp_reg.x
        
        if (i==0 & j==0):
            for k in tqdm(range(num_points)):
                index = helpers.generate_list(betas_reg[i,j,:],int(num_param_keep[k]))
                tmp_sim = lpmc_mnltrain.fit_mle(init, maxiter=maxiter, boxcox=True, reduced=True, indd=index, just_point=True)
                betas_sim[i,j,k,:] = tmp_sim.x
                likelihoodlr[i,j,k] = -1*tmp_sim["fun"]
        else:
            for k in tqdm(range(num_points-1)):
                index = helpers.generate_list(betas_reg[i,j,:],int(num_param_keep[k]))
                tmp_sim = lpmc_mnltrain.fit_mle(init, maxiter=maxiter, boxcox=True, reduced=True, indd=index, just_point=True)
                betas_sim[i,j,k,:] = tmp_sim.x
                likelihoodlr[i,j,k] = -1*tmp_sim["fun"]
            likelihoodlr[i,j,num_points-1] = likelihoodlr[0,0,num_points-1]
                    

# Normalize ll
likelihoodlr=likelihoodlr/(0.25*long_lpmc.shape[0])

sio.savemat("./likelihoodbothlassoridge.mat", mdict={'ll':likelihoodlr})
sio.savemat("./betaGridbothlassoridge.mat", mdict={'beta':betas_reg})
sio.savemat("./betaPointbothlassoridge.mat", mdict={'beta':betas_sim})

beta_simple = betas_sim[0,0,num_points-1]
likelihood_simple = np.ones((num_points))

for k in tqdm(range(num_points-1)):
    index = helpers.generate_list(beta_simple,int(num_param_keep[k]))
    tmp_sim = lpmc_mnltrain.fit_mle(init, maxiter=maxiter, boxcox=True, reduced=True, indd=index, just_point=True)
    likelihood_simple[k] = -1*tmp_sim["fun"]
    
likelihood_simple=likelihood_simple/(0.25*long_lpmc.shape[0])
    
sio.savemat("./likelihood_simple.mat", mdict={'ll':likelihood_simple})


"""
Simulations with random added parameters
Variable :
    Seed = To ensure that the next simulations with more added parameters contains
           the previous added parameters.
"""
seed=[1300,1600,2000, 2500, 3000]
likelihoodrand=np.ones((len(seed)+1,num_points))
for inds,s in enumerate(seed) :
    for k in range(num_points):
        index = helpers.generate_random_list(s,int(num_param_keep[k]))
        b=lpmc_mnltrain.fit_mle(init, maxiter=maxiter, boxcox=True, reduced=True, indd=index, just_point=True)
        likelihoodrand[inds,k]=-1*b["fun"]
likelihoodrand[len(seed),:]=np.mean(likelihoodrand[:len(seed)-1,:],axis=0)


#%%

"""
Load and plot results
Variable : 
    likelihoodend = final log likelihood computes is a maxiter=100 in order 
                    with 483 parameters. Realised with a higher maxiter 
                    because there is more parameters to optimize
"""

likelihoodrand=likelihoodrand.drop(likelihoodrand.shape[0]-1)
finallikelihood = lpmc_mnltrain.fit_mle(init, maxiter=100, boxcox=True, just_point=True)
betanormhist = finallikelihood.x
likelihoodend = -1*finallikelihood["fun"]

#likelihoodend=-0.891829
likelihoodr.loc[:,5]=likelihoodend
likelihoodl.loc[:,5]=likelihoodend
likelihoodrand.loc[:,5]=likelihoodend

x=num_param_keep

fig = plt.figure(1)
ax = fig.add_subplot(1, 1, 1)  

eli = sio.loadmat("./likelihoodbothlassoridge.mat")['ll']
likelihood_better = likelihoodend * np.ones((4, 4))
eli[:,:,5] = likelihood_better

num_points = 6
num_param_keep=np.round(np.logspace(1,np.log10(240),num_points))
num_param_keep[0]=0
lassos = [0.1, 1, 10, 100]
ridges = [0.1, 1, 10, 100]
## SPECIFIC

i = 2
j = 3
y = eli[i,j,:]
lmda_lasso = lassos[i]
lmda_ridge = ridges[j]
plt.plot(x,y,'.',linestyle='-', label = r'($\lambda_L,\lambda_R$)=({1}, {0})'.format(lmda_ridge, lmda_lasso))

i = 2
j = 1
y = eli[i,j,:]
lmda_lasso = lassos[i]
lmda_ridge = ridges[j]
plt.plot(x,y,'.',linestyle='-', label = r'($\lambda_L,\lambda_R$)=({1}, {0})'.format(lmda_ridge, lmda_lasso))         

for j in range(likelihoodrand.shape[0]):
    if(j==(likelihoodrand.shape[0]-1)):
        plt.plot(num_param_keep,likelihoodrand.loc[j,:],'.',linestyle='-', color='black',label ='Averaged random')
    else :
        plt.plot(num_param_keep,likelihoodrand.loc[j,:],'.',color='grey', marker=None,linewidth=0.5,linestyle='-')
plt.plot(num_param_keep,likelihoodl[1,:],'.',linestyle='-', label ='$\lambda_{L}=100$')
plt.plot(num_param_keep,likelihoodr[0,:],'.',linestyle='-', label ='$\lambda_{R}=10$')

plt.grid(True,'major',linestyle='--',linewidth=0.5)
plt.xlabel(r'Added $\beta$ parameters')
plt.ylabel(r'Normalised Log-likelihood')
plt.xticks(num_param_keep)
plt.legend(ncol=1)
plt.show()
fig.savefig('mainplot.png',dpi=500)


"""
Histogram plot
"""

betagrid = sio.loadmat("betaGridbothlassoridge_part2.mat")['beta']
#(10,100)
i = 0
j = 1
y = betagrid[i,j,:]

fig2 = plt.figure(2)
plt.hist(np.abs(y[:243]),bins=10**np.linspace(np.log10(1e-6), np.log10(10),50),histtype='step',alpha=0.5,color='red',linewidth=2,label =  r'($\lambda_L,\lambda_R$)=({1}, {0})'.format(lmda_ridge, lmda_lasso))
plt.hist(np.abs(betanormhist.loc[:243,0]),bins=10**np.linspace(np.log10(1e-6), np.log10(10),50),alpha=1,linewidth=1.5,color='orange',label =r'\noindent Non regularized\\distribution')
plt.hist(np.abs(betasRr[:243,0]),bins=10**np.linspace(np.log10(1e-6), np.log10(10),50),histtype='step',alpha=1,linewidth=1.5,color='blue',label = r'$\lambda_{R}=10$')
plt.hist(np.abs(betasRl[:243,1]),bins=10**np.linspace(np.log10(1e-6), np.log10(10),50),alpha=0.5,color='green',label = r'$\lambda_{L}=100$')


plt.grid(True,'major',linestyle='--',linewidth=0.5)
plt.ylabel(r'Occurencies')
plt.xlabel(r'Parameter estimates (betas, absolute value, log scale)')
#plt.legend(ncol=1,loc='upper left')
plt.gca().set_xscale("log")
plt.gca().legend()
plt.show()
fig2.savefig('histogram.png',dpi=500)


#%%
"""
Out of sample validation over (lambda_L, lambda_R) = (10,1)

The log_likelihood at each point are computed by initializing the model with the beta_sim obtained   
in the Ridge and lasso regularization part. 
The for loop prints the initial log-likelihood, which is the one we are interested in.
These results are manually reported in the lls array
"""


# Generate TEST model

long_lpmc_test = gld.generate_data(train=False)
y = long_lpmc_test.copy()

y.iloc[:, 3::1] = helpers.standardize(long_lpmc_test.iloc[:, 3::1])


choice_column = "travel_mode"
obs_id_column = "custom_id"
custom_alt_id = "mode_id"
basic_specification = helpers.create_specification()

lpmc_mnl = pl.create_choice_model(data=y,
                                        alt_id_col=custom_alt_id,
                                        obs_id_col=obs_id_column,
                                        choice_col=choice_column,
                                        specification=basic_specification,
                                        model_type="MNL",
                                        names=None)

beta_sim = sio.loadmat("./betaPointbothlassoridge.mat")['beta']
# (10,1) ==> i = 2, j=1
i = 2
j = 1
mat = beta_sim[i,j,:]
results = []


for k in range(mat.shape[0]):
    print("k=",k)
    init = mat[k]
    lpmc_mnl.fit_mle(init, maxiter=0, boxcox=True)

lls = np.array([-62090.4712, -59085.4723, -50836.3173, -49499.8913, -48783.4359, -48705.8298])
lls = lls/(0.25*long_lpmc_test.shape[0])

plt.plot(x,lls,'.',linestyle='-', label = r'Test')
plt.grid(True,'major',linestyle='--',linewidth=0.5)
plt.xlabel(r'Added $\beta$ parameters')
plt.ylabel(r'Normalized Log-likelihood')
plt.title(r'$(\lambda_L, \lambda_R)$ = (10,1)')
plt.legend(ncol=1)
plt.xticks(x)
plt.show()