import pandas as pd
import numpy as np
import pylogit as pl
                               
#%%
def generate_data(train=True):
    wide_lpmc = pd.read_table("lpmc.dat", sep="\t")
    
    #%%
    # define travel time for public transport
    #########################################
    wide_lpmc["dur_pt"]=wide_lpmc["dur_pt_access"]+wide_lpmc["dur_pt_rail"]+wide_lpmc["dur_pt_bus"]+wide_lpmc["dur_pt_int"]
    
    # define cost for driving alternative
    #####################################
    wide_lpmc['cost_driving']=wide_lpmc['cost_driving_fuel']+wide_lpmc['cost_driving_ccharge']
    
    # define avaiblity columns 
    ##########################
    wide_lpmc['AV']=np.ones(len(wide_lpmc['cost_driving'])) 
    
    ###############################################
    # SEGMENTATION WRT GENDER, PURPOSE, AGE, SEASON
    ###############################################
    '''
        we copy the columns into segmented ones and put 0 
        when the gender does not match the gender considered in the column.
    '''
    
    # Driving cost male:
    wide_lpmc['cost_driving_male_age1_cold_purpose1'] = wide_lpmc['cost_driving']
    wide_lpmc['cost_driving_male_age1_cold_purpose2'] = wide_lpmc['cost_driving']
    wide_lpmc['cost_driving_male_age1_cold_purpose3'] = wide_lpmc['cost_driving']
    wide_lpmc['cost_driving_male_age1_cold_purpose4'] = wide_lpmc['cost_driving']
    wide_lpmc['cost_driving_male_age1_cold_purpose5'] = wide_lpmc['cost_driving']
    
    wide_lpmc['cost_driving_male_age1_warm_purpose1'] = wide_lpmc['cost_driving']
    wide_lpmc['cost_driving_male_age1_warm_purpose2'] = wide_lpmc['cost_driving']
    wide_lpmc['cost_driving_male_age1_warm_purpose3'] = wide_lpmc['cost_driving']
    wide_lpmc['cost_driving_male_age1_warm_purpose4'] = wide_lpmc['cost_driving']
    wide_lpmc['cost_driving_male_age1_warm_purpose5'] = wide_lpmc['cost_driving']
    
    wide_lpmc['cost_driving_male_age2_cold_purpose1'] = wide_lpmc['cost_driving']
    wide_lpmc['cost_driving_male_age2_cold_purpose2'] = wide_lpmc['cost_driving']
    wide_lpmc['cost_driving_male_age2_cold_purpose3'] = wide_lpmc['cost_driving']
    wide_lpmc['cost_driving_male_age2_cold_purpose4'] = wide_lpmc['cost_driving']
    wide_lpmc['cost_driving_male_age2_cold_purpose5'] = wide_lpmc['cost_driving']
    
    wide_lpmc['cost_driving_male_age2_warm_purpose1'] = wide_lpmc['cost_driving']
    wide_lpmc['cost_driving_male_age2_warm_purpose2'] = wide_lpmc['cost_driving']
    wide_lpmc['cost_driving_male_age2_warm_purpose3'] = wide_lpmc['cost_driving']
    wide_lpmc['cost_driving_male_age2_warm_purpose4'] = wide_lpmc['cost_driving']
    wide_lpmc['cost_driving_male_age2_warm_purpose5'] = wide_lpmc['cost_driving']
    
    wide_lpmc['cost_driving_male_age3_cold_purpose1'] = wide_lpmc['cost_driving']
    wide_lpmc['cost_driving_male_age3_cold_purpose2'] = wide_lpmc['cost_driving']
    wide_lpmc['cost_driving_male_age3_cold_purpose3'] = wide_lpmc['cost_driving']
    wide_lpmc['cost_driving_male_age3_cold_purpose4'] = wide_lpmc['cost_driving']
    wide_lpmc['cost_driving_male_age3_cold_purpose5'] = wide_lpmc['cost_driving']
    
    wide_lpmc['cost_driving_male_age3_warm_purpose1'] = wide_lpmc['cost_driving']
    wide_lpmc['cost_driving_male_age3_warm_purpose2'] = wide_lpmc['cost_driving']
    wide_lpmc['cost_driving_male_age3_warm_purpose3'] = wide_lpmc['cost_driving']
    wide_lpmc['cost_driving_male_age3_warm_purpose4'] = wide_lpmc['cost_driving']
    wide_lpmc['cost_driving_male_age3_warm_purpose5'] = wide_lpmc['cost_driving']
    

    
    # Public transport cost male:
    wide_lpmc['cost_pt_male_age1_cold_purpose1'] = wide_lpmc['cost_transit']
    wide_lpmc['cost_pt_male_age1_cold_purpose2'] = wide_lpmc['cost_transit']
    wide_lpmc['cost_pt_male_age1_cold_purpose3'] = wide_lpmc['cost_transit']
    wide_lpmc['cost_pt_male_age1_cold_purpose4'] = wide_lpmc['cost_transit']
    wide_lpmc['cost_pt_male_age1_cold_purpose5'] = wide_lpmc['cost_transit']
    
    wide_lpmc['cost_pt_male_age1_warm_purpose1'] = wide_lpmc['cost_transit']
    wide_lpmc['cost_pt_male_age1_warm_purpose2'] = wide_lpmc['cost_transit']
    wide_lpmc['cost_pt_male_age1_warm_purpose3'] = wide_lpmc['cost_transit']
    wide_lpmc['cost_pt_male_age1_warm_purpose4'] = wide_lpmc['cost_transit']
    wide_lpmc['cost_pt_male_age1_warm_purpose5'] = wide_lpmc['cost_transit']
    
    wide_lpmc['cost_pt_male_age2_cold_purpose1'] = wide_lpmc['cost_transit']
    wide_lpmc['cost_pt_male_age2_cold_purpose2'] = wide_lpmc['cost_transit']
    wide_lpmc['cost_pt_male_age2_cold_purpose3'] = wide_lpmc['cost_transit']
    wide_lpmc['cost_pt_male_age2_cold_purpose4'] = wide_lpmc['cost_transit']
    wide_lpmc['cost_pt_male_age2_cold_purpose5'] = wide_lpmc['cost_transit']
    
    wide_lpmc['cost_pt_male_age2_warm_purpose1'] = wide_lpmc['cost_transit']
    wide_lpmc['cost_pt_male_age2_warm_purpose2'] = wide_lpmc['cost_transit']
    wide_lpmc['cost_pt_male_age2_warm_purpose3'] = wide_lpmc['cost_transit']
    wide_lpmc['cost_pt_male_age2_warm_purpose4'] = wide_lpmc['cost_transit']
    wide_lpmc['cost_pt_male_age2_warm_purpose5'] = wide_lpmc['cost_transit']
    
    wide_lpmc['cost_pt_male_age3_cold_purpose1'] = wide_lpmc['cost_transit']
    wide_lpmc['cost_pt_male_age3_cold_purpose2'] = wide_lpmc['cost_transit']
    wide_lpmc['cost_pt_male_age3_cold_purpose3'] = wide_lpmc['cost_transit']
    wide_lpmc['cost_pt_male_age3_cold_purpose4'] = wide_lpmc['cost_transit']
    wide_lpmc['cost_pt_male_age3_cold_purpose5'] = wide_lpmc['cost_transit']
    
    wide_lpmc['cost_pt_male_age3_warm_purpose1'] = wide_lpmc['cost_transit']
    wide_lpmc['cost_pt_male_age3_warm_purpose2'] = wide_lpmc['cost_transit']
    wide_lpmc['cost_pt_male_age3_warm_purpose3'] = wide_lpmc['cost_transit']
    wide_lpmc['cost_pt_male_age3_warm_purpose4'] = wide_lpmc['cost_transit']
    wide_lpmc['cost_pt_male_age3_warm_purpose5'] = wide_lpmc['cost_transit']
    

    
    
    # Driving time male:
    wide_lpmc['dur_driving_male_age1_cold_purpose1'] = wide_lpmc['dur_driving']
    wide_lpmc['dur_driving_male_age1_cold_purpose2'] = wide_lpmc['dur_driving']
    wide_lpmc['dur_driving_male_age1_cold_purpose3'] = wide_lpmc['dur_driving']
    wide_lpmc['dur_driving_male_age1_cold_purpose4'] = wide_lpmc['dur_driving']
    wide_lpmc['dur_driving_male_age1_cold_purpose5'] = wide_lpmc['dur_driving']
    
    wide_lpmc['dur_driving_male_age1_warm_purpose1'] = wide_lpmc['dur_driving']
    wide_lpmc['dur_driving_male_age1_warm_purpose2'] = wide_lpmc['dur_driving']
    wide_lpmc['dur_driving_male_age1_warm_purpose3'] = wide_lpmc['dur_driving']
    wide_lpmc['dur_driving_male_age1_warm_purpose4'] = wide_lpmc['dur_driving']
    wide_lpmc['dur_driving_male_age1_warm_purpose5'] = wide_lpmc['dur_driving']
    
    wide_lpmc['dur_driving_male_age2_cold_purpose1'] = wide_lpmc['dur_driving']
    wide_lpmc['dur_driving_male_age2_cold_purpose2'] = wide_lpmc['dur_driving']
    wide_lpmc['dur_driving_male_age2_cold_purpose3'] = wide_lpmc['dur_driving']
    wide_lpmc['dur_driving_male_age2_cold_purpose4'] = wide_lpmc['dur_driving']
    wide_lpmc['dur_driving_male_age2_cold_purpose5'] = wide_lpmc['dur_driving']
    
    wide_lpmc['dur_driving_male_age2_warm_purpose1'] = wide_lpmc['dur_driving']
    wide_lpmc['dur_driving_male_age2_warm_purpose2'] = wide_lpmc['dur_driving']
    wide_lpmc['dur_driving_male_age2_warm_purpose3'] = wide_lpmc['dur_driving']
    wide_lpmc['dur_driving_male_age2_warm_purpose4'] = wide_lpmc['dur_driving']
    wide_lpmc['dur_driving_male_age2_warm_purpose5'] = wide_lpmc['dur_driving']
    
    wide_lpmc['dur_driving_male_age3_cold_purpose1'] = wide_lpmc['dur_driving']
    wide_lpmc['dur_driving_male_age3_cold_purpose2'] = wide_lpmc['dur_driving']
    wide_lpmc['dur_driving_male_age3_cold_purpose3'] = wide_lpmc['dur_driving']
    wide_lpmc['dur_driving_male_age3_cold_purpose4'] = wide_lpmc['dur_driving']
    wide_lpmc['dur_driving_male_age3_cold_purpose5'] = wide_lpmc['dur_driving']
    
    wide_lpmc['dur_driving_male_age3_warm_purpose1'] = wide_lpmc['dur_driving']
    wide_lpmc['dur_driving_male_age3_warm_purpose2'] = wide_lpmc['dur_driving']
    wide_lpmc['dur_driving_male_age3_warm_purpose3'] = wide_lpmc['dur_driving']
    wide_lpmc['dur_driving_male_age3_warm_purpose4'] = wide_lpmc['dur_driving']
    wide_lpmc['dur_driving_male_age3_warm_purpose5'] = wide_lpmc['dur_driving']
    
    

    
    # Public transport time male:
    wide_lpmc['dur_pt_male_age1_cold_purpose1'] = wide_lpmc['dur_pt']
    wide_lpmc['dur_pt_male_age1_cold_purpose2'] = wide_lpmc['dur_pt']
    wide_lpmc['dur_pt_male_age1_cold_purpose3'] = wide_lpmc['dur_pt']
    wide_lpmc['dur_pt_male_age1_cold_purpose4'] = wide_lpmc['dur_pt']
    wide_lpmc['dur_pt_male_age1_cold_purpose5'] = wide_lpmc['dur_pt']
    
    wide_lpmc['dur_pt_male_age1_warm_purpose1'] = wide_lpmc['dur_pt']
    wide_lpmc['dur_pt_male_age1_warm_purpose2'] = wide_lpmc['dur_pt']
    wide_lpmc['dur_pt_male_age1_warm_purpose3'] = wide_lpmc['dur_pt']
    wide_lpmc['dur_pt_male_age1_warm_purpose4'] = wide_lpmc['dur_pt']
    wide_lpmc['dur_pt_male_age1_warm_purpose5'] = wide_lpmc['dur_pt']
    
    wide_lpmc['dur_pt_male_age2_cold_purpose1'] = wide_lpmc['dur_pt']
    wide_lpmc['dur_pt_male_age2_cold_purpose2'] = wide_lpmc['dur_pt']
    wide_lpmc['dur_pt_male_age2_cold_purpose3'] = wide_lpmc['dur_pt']
    wide_lpmc['dur_pt_male_age2_cold_purpose4'] = wide_lpmc['dur_pt']
    wide_lpmc['dur_pt_male_age2_cold_purpose5'] = wide_lpmc['dur_pt']
    
    wide_lpmc['dur_pt_male_age2_warm_purpose1'] = wide_lpmc['dur_pt']
    wide_lpmc['dur_pt_male_age2_warm_purpose2'] = wide_lpmc['dur_pt']
    wide_lpmc['dur_pt_male_age2_warm_purpose3'] = wide_lpmc['dur_pt']
    wide_lpmc['dur_pt_male_age2_warm_purpose4'] = wide_lpmc['dur_pt']
    wide_lpmc['dur_pt_male_age2_warm_purpose5'] = wide_lpmc['dur_pt']
    
    wide_lpmc['dur_pt_male_age3_cold_purpose1'] = wide_lpmc['dur_pt']
    wide_lpmc['dur_pt_male_age3_cold_purpose2'] = wide_lpmc['dur_pt']
    wide_lpmc['dur_pt_male_age3_cold_purpose3'] = wide_lpmc['dur_pt']
    wide_lpmc['dur_pt_male_age3_cold_purpose4'] = wide_lpmc['dur_pt']
    wide_lpmc['dur_pt_male_age3_cold_purpose5'] = wide_lpmc['dur_pt']
    
    wide_lpmc['dur_pt_male_age3_warm_purpose1'] = wide_lpmc['dur_pt']
    wide_lpmc['dur_pt_male_age3_warm_purpose2'] = wide_lpmc['dur_pt']
    wide_lpmc['dur_pt_male_age3_warm_purpose3'] = wide_lpmc['dur_pt']
    wide_lpmc['dur_pt_male_age3_warm_purpose4'] = wide_lpmc['dur_pt']
    wide_lpmc['dur_pt_male_age3_warm_purpose5'] = wide_lpmc['dur_pt']
    
    
    
    # Walking time male:
    wide_lpmc['dur_walking_male_age1_cold_purpose1'] = wide_lpmc['dur_walking']
    wide_lpmc['dur_walking_male_age1_cold_purpose2'] = wide_lpmc['dur_walking']
    wide_lpmc['dur_walking_male_age1_cold_purpose3'] = wide_lpmc['dur_walking']
    wide_lpmc['dur_walking_male_age1_cold_purpose4'] = wide_lpmc['dur_walking']
    wide_lpmc['dur_walking_male_age1_cold_purpose5'] = wide_lpmc['dur_walking']
    
    wide_lpmc['dur_walking_male_age1_warm_purpose1'] = wide_lpmc['dur_walking']
    wide_lpmc['dur_walking_male_age1_warm_purpose2'] = wide_lpmc['dur_walking']
    wide_lpmc['dur_walking_male_age1_warm_purpose3'] = wide_lpmc['dur_walking']
    wide_lpmc['dur_walking_male_age1_warm_purpose4'] = wide_lpmc['dur_walking']
    wide_lpmc['dur_walking_male_age1_warm_purpose5'] = wide_lpmc['dur_walking']
    
    wide_lpmc['dur_walking_male_age2_cold_purpose1'] = wide_lpmc['dur_walking']
    wide_lpmc['dur_walking_male_age2_cold_purpose2'] = wide_lpmc['dur_walking']
    wide_lpmc['dur_walking_male_age2_cold_purpose3'] = wide_lpmc['dur_walking']
    wide_lpmc['dur_walking_male_age2_cold_purpose4'] = wide_lpmc['dur_walking']
    wide_lpmc['dur_walking_male_age2_cold_purpose5'] = wide_lpmc['dur_walking']
    
    wide_lpmc['dur_walking_male_age2_warm_purpose1'] = wide_lpmc['dur_walking']
    wide_lpmc['dur_walking_male_age2_warm_purpose2'] = wide_lpmc['dur_walking']
    wide_lpmc['dur_walking_male_age2_warm_purpose3'] = wide_lpmc['dur_walking']
    wide_lpmc['dur_walking_male_age2_warm_purpose4'] = wide_lpmc['dur_walking']
    wide_lpmc['dur_walking_male_age2_warm_purpose5'] = wide_lpmc['dur_walking']
    
    wide_lpmc['dur_walking_male_age3_cold_purpose1'] = wide_lpmc['dur_walking']
    wide_lpmc['dur_walking_male_age3_cold_purpose2'] = wide_lpmc['dur_walking']
    wide_lpmc['dur_walking_male_age3_cold_purpose3'] = wide_lpmc['dur_walking']
    wide_lpmc['dur_walking_male_age3_cold_purpose4'] = wide_lpmc['dur_walking']
    wide_lpmc['dur_walking_male_age3_cold_purpose5'] = wide_lpmc['dur_walking']
    
    wide_lpmc['dur_walking_male_age3_warm_purpose1'] = wide_lpmc['dur_walking']
    wide_lpmc['dur_walking_male_age3_warm_purpose2'] = wide_lpmc['dur_walking']
    wide_lpmc['dur_walking_male_age3_warm_purpose3'] = wide_lpmc['dur_walking']
    wide_lpmc['dur_walking_male_age3_warm_purpose4'] = wide_lpmc['dur_walking']
    wide_lpmc['dur_walking_male_age3_warm_purpose5'] = wide_lpmc['dur_walking']
    
    

    
    # Cycling time male:
    wide_lpmc['dur_cycling_male_age1_cold_purpose1'] = wide_lpmc['dur_cycling']
    wide_lpmc['dur_cycling_male_age1_cold_purpose2'] = wide_lpmc['dur_cycling']
    wide_lpmc['dur_cycling_male_age1_cold_purpose3'] = wide_lpmc['dur_cycling']
    wide_lpmc['dur_cycling_male_age1_cold_purpose4'] = wide_lpmc['dur_cycling']
    wide_lpmc['dur_cycling_male_age1_cold_purpose5'] = wide_lpmc['dur_cycling']
    
    wide_lpmc['dur_cycling_male_age1_warm_purpose1'] = wide_lpmc['dur_cycling']
    wide_lpmc['dur_cycling_male_age1_warm_purpose2'] = wide_lpmc['dur_cycling']
    wide_lpmc['dur_cycling_male_age1_warm_purpose3'] = wide_lpmc['dur_cycling']
    wide_lpmc['dur_cycling_male_age1_warm_purpose4'] = wide_lpmc['dur_cycling']
    wide_lpmc['dur_cycling_male_age1_warm_purpose5'] = wide_lpmc['dur_cycling']
    
    wide_lpmc['dur_cycling_male_age2_cold_purpose1'] = wide_lpmc['dur_cycling']
    wide_lpmc['dur_cycling_male_age2_cold_purpose2'] = wide_lpmc['dur_cycling']
    wide_lpmc['dur_cycling_male_age2_cold_purpose3'] = wide_lpmc['dur_cycling']
    wide_lpmc['dur_cycling_male_age2_cold_purpose4'] = wide_lpmc['dur_cycling']
    wide_lpmc['dur_cycling_male_age2_cold_purpose5'] = wide_lpmc['dur_cycling']
    
    wide_lpmc['dur_cycling_male_age2_warm_purpose1'] = wide_lpmc['dur_cycling']
    wide_lpmc['dur_cycling_male_age2_warm_purpose2'] = wide_lpmc['dur_cycling']
    wide_lpmc['dur_cycling_male_age2_warm_purpose3'] = wide_lpmc['dur_cycling']
    wide_lpmc['dur_cycling_male_age2_warm_purpose4'] = wide_lpmc['dur_cycling']
    wide_lpmc['dur_cycling_male_age2_warm_purpose5'] = wide_lpmc['dur_cycling']
    
    wide_lpmc['dur_cycling_male_age3_cold_purpose1'] = wide_lpmc['dur_cycling']
    wide_lpmc['dur_cycling_male_age3_cold_purpose2'] = wide_lpmc['dur_cycling']
    wide_lpmc['dur_cycling_male_age3_cold_purpose3'] = wide_lpmc['dur_cycling']
    wide_lpmc['dur_cycling_male_age3_cold_purpose4'] = wide_lpmc['dur_cycling']
    wide_lpmc['dur_cycling_male_age3_cold_purpose5'] = wide_lpmc['dur_cycling']
    
    wide_lpmc['dur_cycling_male_age3_warm_purpose1'] = wide_lpmc['dur_cycling']
    wide_lpmc['dur_cycling_male_age3_warm_purpose2'] = wide_lpmc['dur_cycling']
    wide_lpmc['dur_cycling_male_age3_warm_purpose3'] = wide_lpmc['dur_cycling']
    wide_lpmc['dur_cycling_male_age3_warm_purpose4'] = wide_lpmc['dur_cycling']
    wide_lpmc['dur_cycling_male_age3_warm_purpose5'] = wide_lpmc['dur_cycling']
    

    
    
    # Distance male:
    wide_lpmc['distance_male_age1_cold_purpose1'] = wide_lpmc['distance']
    wide_lpmc['distance_male_age1_cold_purpose2'] = wide_lpmc['distance']
    wide_lpmc['distance_male_age1_cold_purpose3'] = wide_lpmc['distance']
    wide_lpmc['distance_male_age1_cold_purpose4'] = wide_lpmc['distance']
    wide_lpmc['distance_male_age1_cold_purpose5'] = wide_lpmc['distance']
    
    wide_lpmc['distance_male_age1_warm_purpose1'] = wide_lpmc['distance']
    wide_lpmc['distance_male_age1_warm_purpose2'] = wide_lpmc['distance']
    wide_lpmc['distance_male_age1_warm_purpose3'] = wide_lpmc['distance']
    wide_lpmc['distance_male_age1_warm_purpose4'] = wide_lpmc['distance']
    wide_lpmc['distance_male_age1_warm_purpose5'] = wide_lpmc['distance']
    
    wide_lpmc['distance_male_age2_cold_purpose1'] = wide_lpmc['distance']
    wide_lpmc['distance_male_age2_cold_purpose2'] = wide_lpmc['distance']
    wide_lpmc['distance_male_age2_cold_purpose3'] = wide_lpmc['distance']
    wide_lpmc['distance_male_age2_cold_purpose4'] = wide_lpmc['distance']
    wide_lpmc['distance_male_age2_cold_purpose5'] = wide_lpmc['distance']
    
    wide_lpmc['distance_male_age2_warm_purpose1'] = wide_lpmc['distance']
    wide_lpmc['distance_male_age2_warm_purpose2'] = wide_lpmc['distance']
    wide_lpmc['distance_male_age2_warm_purpose3'] = wide_lpmc['distance']
    wide_lpmc['distance_male_age2_warm_purpose4'] = wide_lpmc['distance']
    wide_lpmc['distance_male_age2_warm_purpose5'] = wide_lpmc['distance']
    
    wide_lpmc['distance_male_age3_cold_purpose1'] = wide_lpmc['distance']
    wide_lpmc['distance_male_age3_cold_purpose2'] = wide_lpmc['distance']
    wide_lpmc['distance_male_age3_cold_purpose3'] = wide_lpmc['distance']
    wide_lpmc['distance_male_age3_cold_purpose4'] = wide_lpmc['distance']
    wide_lpmc['distance_male_age3_cold_purpose5'] = wide_lpmc['distance']
    
    wide_lpmc['distance_male_age3_warm_purpose1'] = wide_lpmc['distance']
    wide_lpmc['distance_male_age3_warm_purpose2'] = wide_lpmc['distance']
    wide_lpmc['distance_male_age3_warm_purpose3'] = wide_lpmc['distance']
    wide_lpmc['distance_male_age3_warm_purpose4'] = wide_lpmc['distance']
    wide_lpmc['distance_male_age3_warm_purpose5'] = wide_lpmc['distance']
    
    
    
    ###########
    ## Def Lambdas
    ######
    
    # Distance male:
    wide_lpmc['lambda_male_age1_cold_purpose1'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_male_age1_cold_purpose2'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_male_age1_cold_purpose3'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_male_age1_cold_purpose4'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_male_age1_cold_purpose5'] = np.ones(len(wide_lpmc['cost_driving']))
    
    wide_lpmc['lambda_male_age1_warm_purpose1'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_male_age1_warm_purpose2'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_male_age1_warm_purpose3'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_male_age1_warm_purpose4'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_male_age1_warm_purpose5'] = np.ones(len(wide_lpmc['cost_driving']))
    
    wide_lpmc['lambda_male_age2_cold_purpose1'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_male_age2_cold_purpose2'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_male_age2_cold_purpose3'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_male_age2_cold_purpose4'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_male_age2_cold_purpose5'] = np.ones(len(wide_lpmc['cost_driving']))
    
    wide_lpmc['lambda_male_age2_warm_purpose1'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_male_age2_warm_purpose2'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_male_age2_warm_purpose3'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_male_age2_warm_purpose4'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_male_age2_warm_purpose5'] = np.ones(len(wide_lpmc['cost_driving']))
    
    wide_lpmc['lambda_male_age3_cold_purpose1'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_male_age3_cold_purpose2'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_male_age3_cold_purpose3'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_male_age3_cold_purpose4'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_male_age3_cold_purpose5'] = np.ones(len(wide_lpmc['cost_driving']))
    
    wide_lpmc['lambda_male_age3_warm_purpose1'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_male_age3_warm_purpose2'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_male_age3_warm_purpose3'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_male_age3_warm_purpose4'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_male_age3_warm_purpose5'] = np.ones(len(wide_lpmc['cost_driving']))
    
    
    
    
    
    wide_lpmc['lambda_time_male_age1_cold_purpose1'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_time_male_age1_cold_purpose2'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_time_male_age1_cold_purpose3'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_time_male_age1_cold_purpose4'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_time_male_age1_cold_purpose5'] = np.ones(len(wide_lpmc['cost_driving']))
    
    wide_lpmc['lambda_time_male_age1_warm_purpose1'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_time_male_age1_warm_purpose2'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_time_male_age1_warm_purpose3'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_time_male_age1_warm_purpose4'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_time_male_age1_warm_purpose5'] = np.ones(len(wide_lpmc['cost_driving']))
    
    wide_lpmc['lambda_time_male_age2_cold_purpose1'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_time_male_age2_cold_purpose2'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_time_male_age2_cold_purpose3'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_time_male_age2_cold_purpose4'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_time_male_age2_cold_purpose5'] = np.ones(len(wide_lpmc['cost_driving']))
    
    wide_lpmc['lambda_time_male_age2_warm_purpose1'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_time_male_age2_warm_purpose2'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_time_male_age2_warm_purpose3'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_time_male_age2_warm_purpose4'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_time_male_age2_warm_purpose5'] = np.ones(len(wide_lpmc['cost_driving']))
    
    wide_lpmc['lambda_time_male_age3_cold_purpose1'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_time_male_age3_cold_purpose2'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_time_male_age3_cold_purpose3'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_time_male_age3_cold_purpose4'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_time_male_age3_cold_purpose5'] = np.ones(len(wide_lpmc['cost_driving']))
    
    wide_lpmc['lambda_time_male_age3_warm_purpose1'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_time_male_age3_warm_purpose2'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_time_male_age3_warm_purpose3'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_time_male_age3_warm_purpose4'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_time_male_age3_warm_purpose5'] = np.ones(len(wide_lpmc['cost_driving']))
    
    
    
    wide_lpmc['lambda_cost_male_age1_cold_purpose1'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_cost_male_age1_cold_purpose2'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_cost_male_age1_cold_purpose3'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_cost_male_age1_cold_purpose4'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_cost_male_age1_cold_purpose5'] = np.ones(len(wide_lpmc['cost_driving']))
    
    wide_lpmc['lambda_cost_male_age1_warm_purpose1'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_cost_male_age1_warm_purpose2'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_cost_male_age1_warm_purpose3'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_cost_male_age1_warm_purpose4'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_cost_male_age1_warm_purpose5'] = np.ones(len(wide_lpmc['cost_driving']))
    
    wide_lpmc['lambda_cost_male_age2_cold_purpose1'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_cost_male_age2_cold_purpose2'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_cost_male_age2_cold_purpose3'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_cost_male_age2_cold_purpose4'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_cost_male_age2_cold_purpose5'] = np.ones(len(wide_lpmc['cost_driving']))
    
    wide_lpmc['lambda_cost_male_age2_warm_purpose1'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_cost_male_age2_warm_purpose2'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_cost_male_age2_warm_purpose3'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_cost_male_age2_warm_purpose4'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_cost_male_age2_warm_purpose5'] = np.ones(len(wide_lpmc['cost_driving']))
    
    wide_lpmc['lambda_cost_male_age3_cold_purpose1'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_cost_male_age3_cold_purpose2'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_cost_male_age3_cold_purpose3'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_cost_male_age3_cold_purpose4'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_cost_male_age3_cold_purpose5'] = np.ones(len(wide_lpmc['cost_driving']))
    
    wide_lpmc['lambda_cost_male_age3_warm_purpose1'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_cost_male_age3_warm_purpose2'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_cost_male_age3_warm_purpose3'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_cost_male_age3_warm_purpose4'] = np.ones(len(wide_lpmc['cost_driving']))
    wide_lpmc['lambda_cost_male_age3_warm_purpose5'] = np.ones(len(wide_lpmc['cost_driving']))
    
    
    
    
    #%% FILTERS
        
    
    filter_age1 = wide_lpmc.columns[pd.Series(wide_lpmc.columns).str.contains("age1")]
    filter_age2 = wide_lpmc.columns[pd.Series(wide_lpmc.columns).str.contains("age2")]
    filter_age3 = wide_lpmc.columns[pd.Series(wide_lpmc.columns).str.contains("age3")]
    
    wide_lpmc.loc[(wide_lpmc['age']>18),filter_age1] = 0
    wide_lpmc.loc[((wide_lpmc['age']<=18)&(wide_lpmc['age']>64)),filter_age2] = 0
    wide_lpmc.loc[(wide_lpmc['age']<=64),filter_age3] = 0
    
    filter_warm = wide_lpmc.columns[pd.Series(wide_lpmc.columns).str.contains("warm")]
    filter_cold = wide_lpmc.columns[pd.Series(wide_lpmc.columns).str.contains("cold")]
    
    wide_lpmc.loc[((wide_lpmc['travel_month']!=12)&(wide_lpmc['travel_month']>2)),filter_cold] = 0
    wide_lpmc.loc[((wide_lpmc['travel_month']==12)|(wide_lpmc['travel_month']==1)|(wide_lpmc['travel_month']==2)),filter_warm] = 0
    
    filter_p1 = wide_lpmc.columns[pd.Series(wide_lpmc.columns).str.contains("purpose1")]
    filter_p2 = wide_lpmc.columns[pd.Series(wide_lpmc.columns).str.contains("purpose2")]
    filter_p3 = wide_lpmc.columns[pd.Series(wide_lpmc.columns).str.contains("purpose3")]
    filter_p4 = wide_lpmc.columns[pd.Series(wide_lpmc.columns).str.contains("purpose4")]
    filter_p5 = wide_lpmc.columns[pd.Series(wide_lpmc.columns).str.contains("purpose5")]
    
    wide_lpmc.loc[(wide_lpmc['purpose']!=1),filter_p1] = 0
    wide_lpmc.loc[(wide_lpmc['purpose']!=2),filter_p2] = 0
    wide_lpmc.loc[(wide_lpmc['purpose']!=3),filter_p3] = 0
    wide_lpmc.loc[(wide_lpmc['purpose']!=4),filter_p4] = 0
    wide_lpmc.loc[(wide_lpmc['purpose']!=5),filter_p5] = 0
    
    
    #%%
    # delete useless columns (can be discussed)
    ##############################################
    del wide_lpmc['dur_pt_access']
    del wide_lpmc['dur_pt_rail']
    del wide_lpmc['dur_pt_bus']
    del wide_lpmc['dur_pt_int']
    del wide_lpmc['cost_driving_fuel']
    del wide_lpmc['cost_driving_ccharge']
    del wide_lpmc['driving_license']
    del wide_lpmc['car_ownership']
    del wide_lpmc['trip_id']
    del wide_lpmc['household_id']
    del wide_lpmc['person_n']
    del wide_lpmc['trip_n']
    del wide_lpmc['purpose']
    del wide_lpmc['fueltype']
    del wide_lpmc['faretype']
    del wide_lpmc['bus_scale']
    del wide_lpmc['female']
    del wide_lpmc['pt_interchanges']
    del wide_lpmc['driving_traffic_percent']
    if (train):
        wide_lpmc = wide_lpmc.drop(wide_lpmc[wide_lpmc['survey_year']!=3].index)
    else:
        wide_lpmc = wide_lpmc.drop(wide_lpmc[wide_lpmc['survey_year']==3].index)
    del wide_lpmc['survey_year']
    del wide_lpmc['travel_year']
    del wide_lpmc['travel_month']
    del wide_lpmc['travel_date']
    del wide_lpmc['day_of_week']
    del wide_lpmc['start_time']
    del wide_lpmc['dur_driving']
    del wide_lpmc['dur_walking']
    del wide_lpmc['dur_pt']
    del wide_lpmc['dur_cycling']
    del wide_lpmc['distance']
    del wide_lpmc['cost_driving']
    del wide_lpmc['cost_transit']
    del wide_lpmc['age']
    
    
    
    #%% 
    ''' ind_vars : list of strings.
        Each element should be a column heading in `wide_data` that denotes a
        variable that varies across observations but not across alternatives.
    '''
    
    ind_variables = list(wide_lpmc.columns[pd.Series(wide_lpmc.columns).str.contains("distance")])
    ind_variables = ind_variables + list(wide_lpmc.columns[pd.Series(wide_lpmc.columns).str.contains("lambda")])
    #ind_variables=ind_variables+list(wide_lpmc['survey_year'])
    #%%
    
    
    alt_varying_variables = {
            
            u'travel_time_male_age1_cold_purpose1': dict([(1, 'dur_walking_male_age1_cold_purpose1'),
                                                    (2, 'dur_cycling_male_age1_cold_purpose1'),
                                                    (3, 'dur_pt_male_age1_cold_purpose1'),
                                                    (4, 'dur_driving_male_age1_cold_purpose1')]),
            u'travel_time_male_age1_cold_purpose2': dict([(1, 'dur_walking_male_age1_cold_purpose2'),
                                                    (2, 'dur_cycling_male_age1_cold_purpose2'),
                                                    (3, 'dur_pt_male_age1_cold_purpose2'),
                                                    (4, 'dur_driving_male_age1_cold_purpose2')]),
            u'travel_time_male_age1_cold_purpose3': dict([(1, 'dur_walking_male_age1_cold_purpose3'),
                                                    (2, 'dur_cycling_male_age1_cold_purpose3'),
                                                    (3, 'dur_pt_male_age1_cold_purpose3'),
                                                    (4, 'dur_driving_male_age1_cold_purpose3')]),
            u'travel_time_male_age1_cold_purpose4': dict([(1, 'dur_walking_male_age1_cold_purpose4'),
                                                    (2, 'dur_cycling_male_age1_cold_purpose4'),
                                                    (3, 'dur_pt_male_age1_cold_purpose4'),
                                                    (4, 'dur_driving_male_age1_cold_purpose4')]),
            u'travel_time_male_age1_cold_purpose5': dict([(1, 'dur_walking_male_age1_cold_purpose5'),
                                                    (2, 'dur_cycling_male_age1_cold_purpose5'),
                                                    (3, 'dur_pt_male_age1_cold_purpose5'),
                                                    (4, 'dur_driving_male_age1_cold_purpose5')]),
    
    		u'travel_time_male_age1_warm_purpose1': dict([(1, 'dur_walking_male_age1_warm_purpose1'),
                                                    (2, 'dur_cycling_male_age1_warm_purpose1'),
                                                    (3, 'dur_pt_male_age1_warm_purpose1'),
                                                    (4, 'dur_driving_male_age1_warm_purpose1')]),
            u'travel_time_male_age1_warm_purpose2': dict([(1, 'dur_walking_male_age1_warm_purpose2'),
                                                    (2, 'dur_cycling_male_age1_warm_purpose2'),
                                                    (3, 'dur_pt_male_age1_warm_purpose2'),
                                                    (4, 'dur_driving_male_age1_warm_purpose2')]),
            u'travel_time_male_age1_warm_purpose3': dict([(1, 'dur_walking_male_age1_warm_purpose3'),
                                                    (2, 'dur_cycling_male_age1_warm_purpose3'),
                                                    (3, 'dur_pt_male_age1_warm_purpose3'),
                                                    (4, 'dur_driving_male_age1_warm_purpose3')]),
            u'travel_time_male_age1_warm_purpose4': dict([(1, 'dur_walking_male_age1_warm_purpose4'),
                                                    (2, 'dur_cycling_male_age1_warm_purpose4'),
                                                    (3, 'dur_pt_male_age1_warm_purpose4'),
                                                    (4, 'dur_driving_male_age1_warm_purpose4')]),
            u'travel_time_male_age1_warm_purpose5': dict([(1, 'dur_walking_male_age1_warm_purpose5'),
                                                    (2, 'dur_cycling_male_age1_warm_purpose5'),
                                                    (3, 'dur_pt_male_age1_warm_purpose5'),
                                                    (4, 'dur_driving_male_age1_warm_purpose5')]),
    
    		u'travel_time_male_age2_cold_purpose1': dict([(1, 'dur_walking_male_age2_cold_purpose1'),
                                                    (2, 'dur_cycling_male_age2_cold_purpose1'),
                                                    (3, 'dur_pt_male_age2_cold_purpose1'),
                                                    (4, 'dur_driving_male_age2_cold_purpose1')]),
            u'travel_time_male_age2_cold_purpose2': dict([(1, 'dur_walking_male_age2_cold_purpose2'),
                                                    (2, 'dur_cycling_male_age2_cold_purpose2'),
                                                    (3, 'dur_pt_male_age2_cold_purpose2'),
                                                    (4, 'dur_driving_male_age2_cold_purpose2')]),
            u'travel_time_male_age2_cold_purpose3': dict([(1, 'dur_walking_male_age2_cold_purpose3'),
                                                    (2, 'dur_cycling_male_age2_cold_purpose3'),
                                                    (3, 'dur_pt_male_age2_cold_purpose3'),
                                                    (4, 'dur_driving_male_age2_cold_purpose3')]),
            u'travel_time_male_age2_cold_purpose4': dict([(1, 'dur_walking_male_age2_cold_purpose4'),
                                                    (2, 'dur_cycling_male_age2_cold_purpose4'),
                                                    (3, 'dur_pt_male_age2_cold_purpose4'),
                                                    (4, 'dur_driving_male_age2_cold_purpose4')]),
            u'travel_time_male_age2_cold_purpose5': dict([(1, 'dur_walking_male_age2_cold_purpose5'),
                                                    (2, 'dur_cycling_male_age2_cold_purpose5'),
                                                    (3, 'dur_pt_male_age2_cold_purpose5'),
                                                    (4, 'dur_driving_male_age2_cold_purpose5')]),
    
    		u'travel_time_male_age2_warm_purpose1': dict([(1, 'dur_walking_male_age2_warm_purpose1'),
                                                    (2, 'dur_cycling_male_age2_warm_purpose1'),
                                                    (3, 'dur_pt_male_age2_warm_purpose1'),
                                                    (4, 'dur_driving_male_age2_warm_purpose1')]),
            u'travel_time_male_age2_warm_purpose2': dict([(1, 'dur_walking_male_age2_warm_purpose2'),
                                                    (2, 'dur_cycling_male_age2_warm_purpose2'),
                                                    (3, 'dur_pt_male_age2_warm_purpose2'),
                                                    (4, 'dur_driving_male_age2_warm_purpose2')]),
            u'travel_time_male_age2_warm_purpose3': dict([(1, 'dur_walking_male_age2_warm_purpose3'),
                                                    (2, 'dur_cycling_male_age2_warm_purpose3'),
                                                    (3, 'dur_pt_male_age2_warm_purpose3'),
                                                    (4, 'dur_driving_male_age2_warm_purpose3')]),
            u'travel_time_male_age2_warm_purpose4': dict([(1, 'dur_walking_male_age2_warm_purpose4'),
                                                    (2, 'dur_cycling_male_age2_warm_purpose4'),
                                                    (3, 'dur_pt_male_age2_warm_purpose4'),
                                                    (4, 'dur_driving_male_age2_warm_purpose4')]),
            u'travel_time_male_age2_warm_purpose5': dict([(1, 'dur_walking_male_age2_warm_purpose5'),
                                                    (2, 'dur_cycling_male_age2_warm_purpose5'),
                                                    (3, 'dur_pt_male_age2_warm_purpose5'),
                                                    (4, 'dur_driving_male_age2_warm_purpose5')]),  
    
    		u'travel_time_male_age3_cold_purpose1': dict([(1, 'dur_walking_male_age3_cold_purpose1'),
                                                    (2, 'dur_cycling_male_age3_cold_purpose1'),
                                                    (3, 'dur_pt_male_age3_cold_purpose1'),
                                                    (4, 'dur_driving_male_age3_cold_purpose1')]),
            u'travel_time_male_age3_cold_purpose2': dict([(1, 'dur_walking_male_age3_cold_purpose2'),
                                                    (2, 'dur_cycling_male_age3_cold_purpose2'),
                                                    (3, 'dur_pt_male_age3_cold_purpose2'),
                                                    (4, 'dur_driving_male_age3_cold_purpose2')]),
            u'travel_time_male_age3_cold_purpose3': dict([(1, 'dur_walking_male_age3_cold_purpose3'),
                                                    (2, 'dur_cycling_male_age3_cold_purpose3'),
                                                    (3, 'dur_pt_male_age3_cold_purpose3'),
                                                    (4, 'dur_driving_male_age3_cold_purpose3')]),
            u'travel_time_male_age3_cold_purpose4': dict([(1, 'dur_walking_male_age3_cold_purpose4'),
                                                    (2, 'dur_cycling_male_age3_cold_purpose4'),
                                                    (3, 'dur_pt_male_age3_cold_purpose4'),
                                                    (4, 'dur_driving_male_age3_cold_purpose4')]),
            u'travel_time_male_age3_cold_purpose5': dict([(1, 'dur_walking_male_age3_cold_purpose5'),
                                                    (2, 'dur_cycling_male_age3_cold_purpose5'),
                                                    (3, 'dur_pt_male_age3_cold_purpose5'),
                                                    (4, 'dur_driving_male_age3_cold_purpose5')]),
    
    		u'travel_time_male_age3_warm_purpose1': dict([(1, 'dur_walking_male_age3_warm_purpose1'),
                                                    (2, 'dur_cycling_male_age3_warm_purpose1'),
                                                    (3, 'dur_pt_male_age3_warm_purpose1'),
                                                    (4, 'dur_driving_male_age3_warm_purpose1')]),
            u'travel_time_male_age3_warm_purpose2': dict([(1, 'dur_walking_male_age3_warm_purpose2'),
                                                    (2, 'dur_cycling_male_age3_warm_purpose2'),
                                                    (3, 'dur_pt_male_age3_warm_purpose2'),
                                                    (4, 'dur_driving_male_age3_warm_purpose2')]),
            u'travel_time_male_age3_warm_purpose3': dict([(1, 'dur_walking_male_age3_warm_purpose3'),
                                                    (2, 'dur_cycling_male_age3_warm_purpose3'),
                                                    (3, 'dur_pt_male_age3_warm_purpose3'),
                                                    (4, 'dur_driving_male_age3_warm_purpose3')]),
            u'travel_time_male_age3_warm_purpose4': dict([(1, 'dur_walking_male_age3_warm_purpose4'),
                                                    (2, 'dur_cycling_male_age3_warm_purpose4'),
                                                    (3, 'dur_pt_male_age3_warm_purpose4'),
                                                    (4, 'dur_driving_male_age3_warm_purpose4')]),
            u'travel_time_male_age3_warm_purpose5': dict([(1, 'dur_walking_male_age3_warm_purpose5'),
                                                    (2, 'dur_cycling_male_age3_warm_purpose5'),
                                                    (3, 'dur_pt_male_age3_warm_purpose5'),
                                                    (4, 'dur_driving_male_age3_warm_purpose5')]),  

    
    
            u'travel_cost_male_age1_cold_purpose1': dict([(3, 'cost_pt_male_age1_cold_purpose1'),
    											   (4, 'cost_driving_male_age1_cold_purpose1')]),
            u'travel_cost_male_age1_cold_purpose2': dict([(3, 'cost_pt_male_age1_cold_purpose2'),
    											   (4, 'cost_driving_male_age1_cold_purpose2')]),
            u'travel_cost_male_age1_cold_purpose3': dict([(3, 'cost_pt_male_age1_cold_purpose3'),
    											   (4, 'cost_driving_male_age1_cold_purpose3')]),
            u'travel_cost_male_age1_cold_purpose4': dict([(3, 'cost_pt_male_age1_cold_purpose4'),
    											   (4, 'cost_driving_male_age1_cold_purpose4')]),
            u'travel_cost_male_age1_cold_purpose5': dict([(3, 'cost_pt_male_age1_cold_purpose5'),
    											   (4, 'cost_driving_male_age1_cold_purpose5')]),
    
            u'travel_cost_male_age1_warm_purpose1': dict([(3, 'cost_pt_male_age1_warm_purpose1'),
    											   (4, 'cost_driving_male_age1_warm_purpose1')]),
            u'travel_cost_male_age1_warm_purpose2': dict([(3, 'cost_pt_male_age1_warm_purpose2'),
    											   (4, 'cost_driving_male_age1_warm_purpose2')]),
            u'travel_cost_male_age1_warm_purpose3': dict([(3, 'cost_pt_male_age1_warm_purpose3'),
    											   (4, 'cost_driving_male_age1_warm_purpose3')]),
            u'travel_cost_male_age1_warm_purpose4': dict([(3, 'cost_pt_male_age1_warm_purpose4'),
    											   (4, 'cost_driving_male_age1_warm_purpose4')]),
            u'travel_cost_male_age1_warm_purpose5': dict([(3, 'cost_pt_male_age1_warm_purpose5'),
    											   (4, 'cost_driving_male_age1_warm_purpose5')]),	
    
            u'travel_cost_male_age2_cold_purpose1': dict([(3, 'cost_pt_male_age2_cold_purpose1'),
    											   (4, 'cost_driving_male_age2_cold_purpose1')]),
            u'travel_cost_male_age2_cold_purpose2': dict([(3, 'cost_pt_male_age2_cold_purpose2'),
    											   (4, 'cost_driving_male_age2_cold_purpose2')]),
            u'travel_cost_male_age2_cold_purpose3': dict([(3, 'cost_pt_male_age2_cold_purpose3'),
    											   (4, 'cost_driving_male_age2_cold_purpose3')]),
            u'travel_cost_male_age2_cold_purpose4': dict([(3, 'cost_pt_male_age2_cold_purpose4'),
    											   (4, 'cost_driving_male_age2_cold_purpose4')]),
            u'travel_cost_male_age2_cold_purpose5': dict([(3, 'cost_pt_male_age2_cold_purpose5'),
    											   (4, 'cost_driving_male_age2_cold_purpose5')]),
    
            u'travel_cost_male_age2_warm_purpose1': dict([(3, 'cost_pt_male_age2_warm_purpose1'),
    											   (4, 'cost_driving_male_age2_warm_purpose1')]),
            u'travel_cost_male_age2_warm_purpose2': dict([(3, 'cost_pt_male_age2_warm_purpose2'),
    											   (4, 'cost_driving_male_age2_warm_purpose2')]),
            u'travel_cost_male_age2_warm_purpose3': dict([(3, 'cost_pt_male_age2_warm_purpose3'),
    											   (4, 'cost_driving_male_age2_warm_purpose3')]),
            u'travel_cost_male_age2_warm_purpose4': dict([(3, 'cost_pt_male_age2_warm_purpose4'),
    											   (4, 'cost_driving_male_age2_warm_purpose4')]),
            u'travel_cost_male_age2_warm_purpose5': dict([(3, 'cost_pt_male_age2_warm_purpose5'),
    											   (4, 'cost_driving_male_age2_warm_purpose5')]),
    
            u'travel_cost_male_age3_cold_purpose1': dict([(3, 'cost_pt_male_age3_cold_purpose1'),
    											   (4, 'cost_driving_male_age3_cold_purpose1')]),
            u'travel_cost_male_age3_cold_purpose2': dict([(3, 'cost_pt_male_age3_cold_purpose2'),
    											   (4, 'cost_driving_male_age3_cold_purpose2')]),
            u'travel_cost_male_age3_cold_purpose3': dict([(3, 'cost_pt_male_age3_cold_purpose3'),
    											   (4, 'cost_driving_male_age3_cold_purpose3')]),
            u'travel_cost_male_age3_cold_purpose4': dict([(3, 'cost_pt_male_age3_cold_purpose4'),
    											   (4, 'cost_driving_male_age3_cold_purpose4')]),
            u'travel_cost_male_age3_cold_purpose5': dict([(3, 'cost_pt_male_age3_cold_purpose5'),
    											   (4, 'cost_driving_male_age3_cold_purpose5')]),
    
            u'travel_cost_male_age3_warm_purpose1': dict([(3, 'cost_pt_male_age3_warm_purpose1'),
    											   (4, 'cost_driving_male_age3_warm_purpose1')]),
            u'travel_cost_male_age3_warm_purpose2': dict([(3, 'cost_pt_male_age3_warm_purpose2'),
    											   (4, 'cost_driving_male_age3_warm_purpose2')]),
            u'travel_cost_male_age3_warm_purpose3': dict([(3, 'cost_pt_male_age3_warm_purpose3'),
    											   (4, 'cost_driving_male_age3_warm_purpose3')]),
            u'travel_cost_male_age3_warm_purpose4': dict([(3, 'cost_pt_male_age3_warm_purpose4'),
    											   (4, 'cost_driving_male_age3_warm_purpose4')]),
            u'travel_cost_male_age3_warm_purpose5': dict([(3, 'cost_pt_male_age3_warm_purpose5'),
    											   (4, 'cost_driving_male_age3_warm_purpose5')]),	
    						   
    
    }
    
    
    #%%
    
    availability_variables = {1: 'AV',
                              2: 'AV', 
                              3: 'AV',
                              4: 'AV'}
    
    custom_alt_id = "mode_id"
    
    # obs_id_column = "trip_id"
    # wide_lpmc["trip_id"] =wide_lpmc["trip_id"]+1
    
    obs_id_column = "custom_id"
    wide_lpmc[obs_id_column] = np.arange(wide_lpmc.shape[0],
                                                dtype=int) + 1
    
    
    
    
    
    # Create a variable recording the choice column
    choice_column = "travel_mode"
    
    
    
    long_lpmc = pl.convert_wide_to_long(wide_lpmc,ind_variables, alt_varying_variables, availability_variables, 
                                                obs_id_column, 
                                                choice_column,new_alt_id_name=custom_alt_id)
    
    return long_lpmc


