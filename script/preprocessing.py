import os
import utils
# import dotenv
# import umap
import pandas as pd
import numpy as np
import dataextraction as de
# import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
# from sklearn.decomposition import PCA
# from sklearn.manifold import TSNE
# from sklearn.mixture import GaussianMixture
# from sklearn.cluster import DBSCAN, SpectralClustering, KMeans, Birch
# import hdbscan

def load_data():  
    conn = de.connect_to_database()
    df = de.get_base_dataset(conn, "base_dataset_v2")
    return df

def check_duplicate_patient(df, cache=False, verbose=False):    
    duplicate_num = df['subject_id'].duplicated().sum()
    if(duplicate_num > 0):
        if(verbose):
            print(f"Shape of the dataset {df.shape}")            
            print("Getting duplicate subjects...")
            print("Number of duplicate subjects {}".format(duplicate_num))
        if(cache):
            utils.cache_database(df)
    else:
        print("No duplicate subjects")
    return df

def get_first_icu_stay(df, cache=False, verbose=False):    
    df = df[df['first_icu_stay'] == True]
    if(verbose):
        print(f"Shape of the dataset {df.shape}")        
        print("Getting first ICU stay...")
        print("Number of rows {}".format(len(df)))
    if(cache):
        utils.cache_database(df)
    return df

def aggregate_missing_mean_columns(df, cache=False, verbose=False):
    missing_mean_columns = utils.detect_missing_mean_columns(df)
    df = utils.add_missing_mean_columns(df, missing_mean_columns)
    if(verbose):
        print(f"Shape of the dataset {df.shape}")       
        print("Aggregating missing mean columns...")
        print("Number of rows {}".format(len(df)))
        for col in missing_mean_columns:
            print("Added column {}".format(col[1]))
    if(cache):
        utils.cache_database(df)
    return df

def aggregate_repeated_mean_measuremenets(df, cache=False, verbose=False):
    mean_columns = [col for col in df.columns if '_mean' in col]
    aggregation_functions = {}
    for col in mean_columns:
        aggregation_functions[col] = 'mean'

    df_aggregated = df.groupby('subject_id').agg(aggregation_functions).reset_index()

    other_columns = [col for col in df.columns if('_mean' not in col and '_min' not in col and '_max' not in col)]
    df_other_columns = df.groupby('subject_id', as_index=False)[other_columns].first()
    df = pd.merge(df_aggregated, df_other_columns, on='subject_id')
    if(verbose):
        print(f"Shape of the dataset {df.shape}")       
        print("Aggregating repeated mean measurements...")
        print("Number of rows {}".format(len(df)))
        for col in df_aggregated.columns:
            print("Aggregated column {}".format(col))                    
    if(cache):
        utils.cache_database(df)        
    return df

def aggregate_score_to_mortality(df, cache=False, verbose=False):    
    def map_lods(score):
     logit = -3.4043 + 0.4173 * (score)
     return (np.exp(logit)) / (1 + np.exp(logit)) 
        
    df['mr_lods'] = df['lods'].apply(map_lods)    
    if(verbose):
        print(f"Shape of the dataset {df.shape}")       
        print("Aggregating score to mortality...")
        print("Number of rows {}".format(len(df)))
        print("Aggregated column mr_lods")
    if(cache):
        utils.cache_database(df)        
    return df

def remove_unecessary_columns(df, columns_to_remove, cache=False, verbose=False):    
    df = df.drop(columns_to_remove, axis=1)
    if(verbose):
        print(f"Shape of the dataset {df.shape}")   
        print("Removing unecessary columns...")
        print("Number of rows {}".format(len(df)))
        for col in columns_to_remove:
            print("Removed column {}".format(col))
    if(cache):
        utils.cache_database(df)
    return df

def remove_features_with_most_null(df, cache=False, verbose=False):
    columns_to_remove = []
    for key, value in df.isnull().sum().to_dict().items():
        if(((value / df.shape[0]) * 100) > 50):
            print(key, value)
            columns_to_remove.append(key)
    if(columns_to_remove == []):
        print("No columns to remove")
    df = df.drop(columns_to_remove, axis=1)
    if(verbose):
        print(f"Shape of the dataset {df.shape}")      
        print("Removing features with most null...")
        print("Number of rows {}".format(len(df)))
        for col in columns_to_remove:
            print("Removed column {}".format(col))
    if(cache):
        utils.cache_database(df)
    return df

def encode_binary(df, columns_to_encode, cache=False, verbose=False):
    for col in columns_to_encode:
        df[col] = df[col].map({'M': 0, 'F': 1})
    if(verbose):
        print(f"Shape of the dataset {df.shape}")  
        print("Encoding binary...")
        print("Number of rows {}".format(len(df)))
        for col in columns_to_encode:
            print("Encoded column {}".format(col))
    if(cache):
        utils.cache_database(df)
    return df

def encode_frequency(df, columns_to_encode, cache=False, verbose=False):
    for col in columns_to_encode:
        frequency_mapping = df[col].value_counts(normalize=True)
        df[col] = df[col].map(frequency_mapping)
    if(verbose):
        print(f"Shape of the dataset {df.shape}")
        print("Encoding frequency...")
        print("Number of rows {}".format(len(df)))
        for col in columns_to_encode:
            print("Encoded column {}".format(col))
    if(cache):
        utils.cache_database(df)
    return df

def encode_one_hot(df, columns_to_encode, cache=False, verbose=False):
    df = pd.get_dummies(df, columns=columns_to_encode)
    if(verbose):
        print(f"Shape of the dataset {df.shape}")      
        print("Encoding one hot...")
        print("Number of rows {}".format(len(df)))
        for col in columns_to_encode:
            print("Encoded column {}".format(col))
    if(cache):
        utils.cache_database(df)
    return df
        
def drop_rows_including_null(df, cache=False, verbose=False):
    df = df.dropna()
    if(verbose):
        print(f"Shape of the dataset {df.shape}")
        print("Dropping rows including null...")
        print("Number of rows {}".format(len(df)))
    if(cache):
        utils.cache_database(df)
    return df

def standard_scale_data(df, cache=False, verbose=False):
    scaler = StandardScaler()
    df = scaler.fit_transform(df)
    if(verbose):
        print(f"Shape of the dataset {df.shape}")   
        print("Number of rows {}".format(len(df)))
        print("Data {}".format(df))
        print("Data shape {}".format(df.shape))
        print("Data type {}".format(type(df)))
        
    if(cache):
        utils.cache_database(df)
    return df

def map_mortality_rate_to_icu_level(df, cache=False, verbose=False):
    def map_mortality_rate_to_level(mortality_rate):    
        if 0 < mortality_rate < 0.33:
            return 'Level 1'
        elif 0.33 <= mortality_rate < 0.66:
            return 'Level 2'
        elif 0.66 <= mortality_rate < 0.99:
            return 'Level 3'
        else:
            return 'Unknown'

    df['icu_level'] = df['mr_lods'].apply(map_mortality_rate_to_level)
    if(verbose):
        print(f"Shape of the dataset {df.shape}")
        print("Mapping mortality rate to ICU level...")
        print("Number of rows {}".format(len(df)))
        print("Mapped column icu_level")
    if(cache):
        utils.cache_database(df)
    return df



columns_to_remove = ['intime', 'outtime', 'dod', 
                     'admittime', 'dischtime', 'deathtime', 
                     'edregtime', 'edouttime', 'language', 'religion', 
                     'ethnicity', 'dbsource']
columns_to_binary_encode = ['gender']
columns_to_frequency_encode = ['diagnosis']
columns_to_one_hot_encode = ['marital_status', 'ethnicity_grouped', 'first_careunit', 
                             'last_careunit', 'admission_type', 'admission_location', 
                             'discharge_location', 'insurance']

preprocessing_pipeline = [
    ('Check duplicate patients', check_duplicate_patient, {'cache': False, 'verbose': True}),
    ('Get first ICU stay', get_first_icu_stay, {'cache': False, 'verbose': True}),
    ('Aggregate missing mean columns', aggregate_missing_mean_columns, {'cache': False, 'verbose': True}),
    ('Aggregate repeated mean measurements', aggregate_repeated_mean_measuremenets, {'cache': False, 'verbose': True}),
    ('Remove unecessary columns', remove_unecessary_columns, {'columns_to_remove': columns_to_remove, 'cache': False, 'verbose': True}),
    ('Remove features with most null', remove_features_with_most_null, {'cache': False, 'verbose': True}),
    ('Binary encoding', encode_binary, {'columns_to_encode': columns_to_binary_encode, 'cache': False, 'verbose': True}),
    ('Frequency encoding', encode_frequency, {'columns_to_encode': columns_to_frequency_encode, 'cache': False, 'verbose': True}),
    ('One-hot encode', encode_one_hot, {'columns_to_encode': columns_to_one_hot_encode, 'cache': False, 'verbose': True}),
    ('Drop rows including null', drop_rows_including_null, {'cache': True, 'verbose': True}),
    # ('Aggregate score to mortality', aggregate_score_to_mortality, {'cache': False, 'verbose': True}),
    # ('Map mortality rate to ICU level', map_mortality_rate_to_icu_level, {'cache': True, 'verbose': True}),
    ('Check duplicate patients', check_duplicate_patient, {'cache': False, 'verbose': True}),
    # ('Standard scale data', standard_scale_data, {'cache': False, 'verbose': True}),
]

def run_preprocessing_pipeline(df, pipeline=preprocessing_pipeline):
    for step_name, step_function, step_params in pipeline:
        print("\n\n")
        print("Running step {}".format(step_name))
        df = step_function(df, **step_params)
    if(type(df) != type(pd.DataFrame())):
        print("Warning, dataframe is not of type pandas.DataFrame")
    return df


