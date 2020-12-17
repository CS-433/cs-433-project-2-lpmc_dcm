
import pylogit
from collections import OrderedDict
from sklearn import preprocessing
import numpy as np
import pandas as pd


def generate_random_list(seed, nparam):
    tmp = np.arange(240)
    np.random.seed(seed) 
    np.random.shuffle(tmp)
    important_beta  = 3 + tmp[:nparam]
    important_lmda  = 243 + important_beta
    asc = [0,1,2]
    return asc + np.ndarray.tolist(important_beta) + np.ndarray.tolist(important_lmda)


def generate_list(beta, nparam):
    sorted_args = np.argsort(np.abs(beta[3:243]))[::-1]
    important_beta  = 3 + sorted_args[:nparam]
    important_lmda  = 243 + important_beta
    asc = [0,1,2]
    return asc + np.ndarray.tolist(important_beta) + np.ndarray.tolist(important_lmda)

def standardize(y): 
    x=y.values;
    min_max_scaler=preprocessing.MinMaxScaler()
    x_scaled=min_max_scaler.fit_transform(x)
    y.loc[:,:]=x_scaled
    return y

def sorting_betas_args(index):
    return np.argsort(np.abs(betas[3:243,index]))[::-1]

def create_specification():

    basic_specification = OrderedDict()
    basic_names = OrderedDict()
    
    basic_specification["intercept"] = [2, 3, 4]
    basic_names["intercept"] = ['ASC Cycle',
                                'ASC PT',
                                'ASC Car']
    
    
    basic_specification['distance_male_age1_cold_purpose1'] =  [[2 ,3 ,4]]
    basic_specification['distance_male_age1_cold_purpose2'] =  [[2 ,3 ,4]]
    basic_specification['distance_male_age1_cold_purpose3'] =  [[2 ,3 ,4]]
    basic_specification['distance_male_age1_cold_purpose4'] =  [[2 ,3 ,4]]
    basic_specification['distance_male_age1_cold_purpose5'] =  [[2 ,3 ,4]]
    
    basic_specification['distance_male_age1_warm_purpose1'] =  [[2 ,3 ,4]]
    basic_specification['distance_male_age1_warm_purpose2'] =  [[2 ,3 ,4]]
    basic_specification['distance_male_age1_warm_purpose3'] =  [[2 ,3 ,4]]
    basic_specification['distance_male_age1_warm_purpose4'] =  [[2 ,3 ,4]]
    basic_specification['distance_male_age1_warm_purpose5'] =  [[2 ,3 ,4]]
    
    basic_specification['distance_male_age2_cold_purpose1'] =  [[2 ,3 ,4]]
    basic_specification['distance_male_age2_cold_purpose2'] =  [[2 ,3 ,4]]
    basic_specification['distance_male_age2_cold_purpose3'] =  [[2 ,3 ,4]]
    basic_specification['distance_male_age2_cold_purpose4'] =  [[2 ,3 ,4]]
    basic_specification['distance_male_age2_cold_purpose5'] =  [[2 ,3 ,4]]
    
    basic_specification['distance_male_age2_warm_purpose1'] =  [[2 ,3 ,4]]
    basic_specification['distance_male_age2_warm_purpose2'] =  [[2 ,3 ,4]]
    basic_specification['distance_male_age2_warm_purpose3'] =  [[2 ,3 ,4]]
    basic_specification['distance_male_age2_warm_purpose4'] =  [[2 ,3 ,4]]
    basic_specification['distance_male_age2_warm_purpose5'] =  [[2 ,3 ,4]]
    
    basic_specification['distance_male_age3_cold_purpose1'] =  [[2 ,3 ,4]]
    basic_specification['distance_male_age3_cold_purpose2'] =  [[2 ,3 ,4]]
    basic_specification['distance_male_age3_cold_purpose3'] =  [[2 ,3 ,4]]
    basic_specification['distance_male_age3_cold_purpose4'] =  [[2 ,3 ,4]]
    basic_specification['distance_male_age3_cold_purpose5'] =  [[2 ,3 ,4]]
    
    basic_specification['distance_male_age3_warm_purpose1'] =  [[2 ,3 ,4]]
    basic_specification['distance_male_age3_warm_purpose2'] =  [[2 ,3 ,4]]
    basic_specification['distance_male_age3_warm_purpose3'] =  [[2 ,3 ,4]]
    basic_specification['distance_male_age3_warm_purpose4'] =  [[2 ,3 ,4]]
    basic_specification['distance_male_age3_warm_purpose5'] =  [[2 ,3 ,4]]
    
    
    
    
    basic_specification['travel_time_male_age1_cold_purpose1'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_time_male_age1_cold_purpose2'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_time_male_age1_cold_purpose3'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_time_male_age1_cold_purpose4'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_time_male_age1_cold_purpose5'] =  [1 ,2 ,3 ,4]
    
    basic_specification['travel_time_male_age1_warm_purpose1'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_time_male_age1_warm_purpose2'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_time_male_age1_warm_purpose3'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_time_male_age1_warm_purpose4'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_time_male_age1_warm_purpose5'] =  [1 ,2 ,3 ,4]
    
    basic_specification['travel_time_male_age2_cold_purpose1'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_time_male_age2_cold_purpose2'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_time_male_age2_cold_purpose3'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_time_male_age2_cold_purpose4'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_time_male_age2_cold_purpose5'] =  [1 ,2 ,3 ,4]
    
    basic_specification['travel_time_male_age2_warm_purpose1'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_time_male_age2_warm_purpose2'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_time_male_age2_warm_purpose3'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_time_male_age2_warm_purpose4'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_time_male_age2_warm_purpose5'] =  [1 ,2 ,3 ,4]
    
    basic_specification['travel_time_male_age3_cold_purpose1'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_time_male_age3_cold_purpose2'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_time_male_age3_cold_purpose3'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_time_male_age3_cold_purpose4'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_time_male_age3_cold_purpose5'] =  [1 ,2 ,3 ,4]
    
    basic_specification['travel_time_male_age3_warm_purpose1'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_time_male_age3_warm_purpose2'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_time_male_age3_warm_purpose3'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_time_male_age3_warm_purpose4'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_time_male_age3_warm_purpose5'] =  [1 ,2 ,3 ,4]
    
    
    
    basic_specification['travel_cost_male_age1_cold_purpose1'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_cost_male_age1_cold_purpose2'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_cost_male_age1_cold_purpose3'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_cost_male_age1_cold_purpose4'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_cost_male_age1_cold_purpose5'] =  [1 ,2 ,3 ,4]
    
    basic_specification['travel_cost_male_age1_warm_purpose1'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_cost_male_age1_warm_purpose2'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_cost_male_age1_warm_purpose3'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_cost_male_age1_warm_purpose4'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_cost_male_age1_warm_purpose5'] =  [1 ,2 ,3 ,4]
    
    basic_specification['travel_cost_male_age2_cold_purpose1'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_cost_male_age2_cold_purpose2'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_cost_male_age2_cold_purpose3'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_cost_male_age2_cold_purpose4'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_cost_male_age2_cold_purpose5'] =  [1 ,2 ,3 ,4]
    
    basic_specification['travel_cost_male_age2_warm_purpose1'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_cost_male_age2_warm_purpose2'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_cost_male_age2_warm_purpose3'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_cost_male_age2_warm_purpose4'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_cost_male_age2_warm_purpose5'] =  [1 ,2 ,3 ,4]
    
    basic_specification['travel_cost_male_age3_cold_purpose1'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_cost_male_age3_cold_purpose2'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_cost_male_age3_cold_purpose3'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_cost_male_age3_cold_purpose4'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_cost_male_age3_cold_purpose5'] =  [1 ,2 ,3 ,4]
    
    basic_specification['travel_cost_male_age3_warm_purpose1'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_cost_male_age3_warm_purpose2'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_cost_male_age3_warm_purpose3'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_cost_male_age3_warm_purpose4'] =  [1 ,2 ,3 ,4]
    basic_specification['travel_cost_male_age3_warm_purpose5'] =  [1 ,2 ,3 ,4]
    
    #basic_specification["age"] = [[2, 3, 4]]
    #basic_names["age"] = ['Age, units: yrs']
    
    #############
    # Instanciation des Lambdas
    
    
    basic_specification['lambda_male_age1_cold_purpose1'] =  [[2 ,3 ,4]]
    basic_specification['lambda_male_age1_cold_purpose2'] =  [[2 ,3 ,4]]
    basic_specification['lambda_male_age1_cold_purpose3'] =  [[2 ,3 ,4]]
    basic_specification['lambda_male_age1_cold_purpose4'] =  [[2 ,3 ,4]]
    basic_specification['lambda_male_age1_cold_purpose5'] =  [[2 ,3 ,4]]
    
    basic_specification['lambda_male_age1_warm_purpose1'] =  [[2 ,3 ,4]]
    basic_specification['lambda_male_age1_warm_purpose2'] =  [[2 ,3 ,4]]
    basic_specification['lambda_male_age1_warm_purpose3'] =  [[2 ,3 ,4]]
    basic_specification['lambda_male_age1_warm_purpose4'] =  [[2 ,3 ,4]]
    basic_specification['lambda_male_age1_warm_purpose5'] =  [[2 ,3 ,4]]
    
    basic_specification['lambda_male_age2_cold_purpose1'] =  [[2 ,3 ,4]]
    basic_specification['lambda_male_age2_cold_purpose2'] =  [[2 ,3 ,4]]
    basic_specification['lambda_male_age2_cold_purpose3'] =  [[2 ,3 ,4]]
    basic_specification['lambda_male_age2_cold_purpose4'] =  [[2 ,3 ,4]]
    basic_specification['lambda_male_age2_cold_purpose5'] =  [[2 ,3 ,4]]
    
    basic_specification['lambda_male_age2_warm_purpose1'] =  [[2 ,3 ,4]]
    basic_specification['lambda_male_age2_warm_purpose2'] =  [[2 ,3 ,4]]
    basic_specification['lambda_male_age2_warm_purpose3'] =  [[2 ,3 ,4]]
    basic_specification['lambda_male_age2_warm_purpose4'] =  [[2 ,3 ,4]]
    basic_specification['lambda_male_age2_warm_purpose5'] =  [[2 ,3 ,4]]
    
    basic_specification['lambda_male_age3_cold_purpose1'] =  [[2 ,3 ,4]]
    basic_specification['lambda_male_age3_cold_purpose2'] =  [[2 ,3 ,4]]
    basic_specification['lambda_male_age3_cold_purpose3'] =  [[2 ,3 ,4]]
    basic_specification['lambda_male_age3_cold_purpose4'] =  [[2 ,3 ,4]]
    basic_specification['lambda_male_age3_cold_purpose5'] =  [[2 ,3 ,4]]
    
    basic_specification['lambda_male_age3_warm_purpose1'] =  [[2 ,3 ,4]]
    basic_specification['lambda_male_age3_warm_purpose2'] =  [[2 ,3 ,4]]
    basic_specification['lambda_male_age3_warm_purpose3'] =  [[2 ,3 ,4]]
    basic_specification['lambda_male_age3_warm_purpose4'] =  [[2 ,3 ,4]]
    basic_specification['lambda_male_age3_warm_purpose5'] =  [[2 ,3 ,4]]
    

    
    

    
    
    basic_specification['lambda_time_male_age1_cold_purpose1'] =  [1, 2, 3, 4]
    basic_specification['lambda_time_male_age1_cold_purpose2'] =  [1, 2, 3, 4]
    basic_specification['lambda_time_male_age1_cold_purpose3'] =  [1, 2, 3, 4]
    basic_specification['lambda_time_male_age1_cold_purpose4'] =  [1, 2, 3, 4]
    basic_specification['lambda_time_male_age1_cold_purpose5'] =  [1, 2, 3, 4]
    
    basic_specification['lambda_time_male_age1_warm_purpose1'] =  [1, 2, 3, 4]
    basic_specification['lambda_time_male_age1_warm_purpose2'] =  [1, 2, 3, 4]
    basic_specification['lambda_time_male_age1_warm_purpose3'] =  [1, 2, 3, 4]
    basic_specification['lambda_time_male_age1_warm_purpose4'] =  [1, 2, 3, 4]
    basic_specification['lambda_time_male_age1_warm_purpose5'] =  [1, 2, 3, 4]
    
    basic_specification['lambda_time_male_age2_cold_purpose1'] =  [1, 2, 3, 4]
    basic_specification['lambda_time_male_age2_cold_purpose2'] =  [1, 2, 3, 4]
    basic_specification['lambda_time_male_age2_cold_purpose3'] =  [1, 2, 3, 4]
    basic_specification['lambda_time_male_age2_cold_purpose4'] =  [1, 2, 3, 4]
    basic_specification['lambda_time_male_age2_cold_purpose5'] =  [1, 2, 3, 4]
    
    basic_specification['lambda_time_male_age2_warm_purpose1'] =  [1, 2, 3, 4]
    basic_specification['lambda_time_male_age2_warm_purpose2'] =  [1, 2, 3, 4]
    basic_specification['lambda_time_male_age2_warm_purpose3'] =  [1, 2, 3, 4]
    basic_specification['lambda_time_male_age2_warm_purpose4'] =  [1, 2, 3, 4]
    basic_specification['lambda_time_male_age2_warm_purpose5'] =  [1, 2, 3, 4]
    
    basic_specification['lambda_time_male_age3_cold_purpose1'] =  [1, 2, 3, 4]
    basic_specification['lambda_time_male_age3_cold_purpose2'] =  [1, 2, 3, 4]
    basic_specification['lambda_time_male_age3_cold_purpose3'] =  [1, 2, 3, 4]
    basic_specification['lambda_time_male_age3_cold_purpose4'] =  [1, 2, 3, 4]
    basic_specification['lambda_time_male_age3_cold_purpose5'] =  [1, 2, 3, 4]
    
    basic_specification['lambda_time_male_age3_warm_purpose1'] =  [1, 2, 3, 4]
    basic_specification['lambda_time_male_age3_warm_purpose2'] =  [1, 2, 3, 4]
    basic_specification['lambda_time_male_age3_warm_purpose3'] =  [1, 2, 3, 4]
    basic_specification['lambda_time_male_age3_warm_purpose4'] =  [1, 2, 3, 4]
    basic_specification['lambda_time_male_age3_warm_purpose5'] =  [1, 2, 3, 4]
    
    
    
    basic_specification['lambda_cost_male_age1_cold_purpose1'] =  [3, 4]
    basic_specification['lambda_cost_male_age1_cold_purpose2'] =  [3, 4]
    basic_specification['lambda_cost_male_age1_cold_purpose3'] =  [3, 4]
    basic_specification['lambda_cost_male_age1_cold_purpose4'] =  [3, 4]
    basic_specification['lambda_cost_male_age1_cold_purpose5'] =  [3, 4]
    
    basic_specification['lambda_cost_male_age1_warm_purpose1'] =  [3, 4]
    basic_specification['lambda_cost_male_age1_warm_purpose2'] =  [3, 4]
    basic_specification['lambda_cost_male_age1_warm_purpose3'] =  [3, 4]
    basic_specification['lambda_cost_male_age1_warm_purpose4'] =  [3, 4]
    basic_specification['lambda_cost_male_age1_warm_purpose5'] =  [3, 4]
    
    basic_specification['lambda_cost_male_age2_cold_purpose1'] =  [3, 4]
    basic_specification['lambda_cost_male_age2_cold_purpose2'] =  [3, 4]
    basic_specification['lambda_cost_male_age2_cold_purpose3'] =  [3, 4]
    basic_specification['lambda_cost_male_age2_cold_purpose4'] =  [3, 4]
    basic_specification['lambda_cost_male_age2_cold_purpose5'] =  [3, 4]
    
    basic_specification['lambda_cost_male_age2_warm_purpose1'] =  [3, 4]
    basic_specification['lambda_cost_male_age2_warm_purpose2'] =  [3, 4]
    basic_specification['lambda_cost_male_age2_warm_purpose3'] =  [3, 4]
    basic_specification['lambda_cost_male_age2_warm_purpose4'] =  [3, 4]
    basic_specification['lambda_cost_male_age2_warm_purpose5'] =  [3, 4]
    
    basic_specification['lambda_cost_male_age3_cold_purpose1'] =  [3, 4]
    basic_specification['lambda_cost_male_age3_cold_purpose2'] =  [3, 4]
    basic_specification['lambda_cost_male_age3_cold_purpose3'] =  [3, 4]
    basic_specification['lambda_cost_male_age3_cold_purpose4'] =  [3, 4]
    basic_specification['lambda_cost_male_age3_cold_purpose5'] =  [3, 4]
    
    basic_specification['lambda_cost_male_age3_warm_purpose1'] =  [3, 4]
    basic_specification['lambda_cost_male_age3_warm_purpose2'] =  [3, 4]
    basic_specification['lambda_cost_male_age3_warm_purpose3'] =  [3, 4]
    basic_specification['lambda_cost_male_age3_warm_purpose4'] =  [3, 4]
    basic_specification['lambda_cost_male_age3_warm_purpose5'] =  [3, 4]
    
    return basic_specification