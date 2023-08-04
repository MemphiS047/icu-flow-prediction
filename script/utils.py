import dataextraction as de
import mrmapping as mr
import numpy as np
import dotenv
import os

dotenv.load_dotenv()

def detect_missing_mean_columns(df):
    missing_mean_cols = []
    for column in df.columns:
        if '_min' in column and column.replace('_min', '_max') in df.columns:
            mean_column = column.replace('_min', '_mean')
            if mean_column not in df.columns:
                missing_mean_cols.append((column, mean_column))
    return missing_mean_cols

def calculate_mean(row, min_col, max_col):
    return (row[min_col] + row[max_col]) / 2


def add_missing_mean_columns(df, missing_mean_cols):
    for min_col, mean_col in missing_mean_cols:
        df.loc[:, mean_col] = df.apply(lambda row: calculate_mean(row, min_col, min_col.replace('_min', '_max')), axis=1)
    return df


def remove_min_max_columns(df):
    mean_columns = [col for col in df.columns if '_mean' in col]
    df = df[mean_columns]
    return df

def get_one_to_many_relationship_columns(df):
    subject_id_counts = df.groupby('subject_id').size()    
    one_to_many_subject_ids = subject_id_counts[subject_id_counts > 1].index.tolist()    
    one_to_many_df = df[df['subject_id'].isin(one_to_many_subject_ids)]    
    one_to_many_columns = list(one_to_many_df.columns)    
    one_to_many_columns.remove('subject_id')
    return one_to_many_columns

def aggregate_score_to_mortality():
    conn = de.connect_to_database()
    df = de.get_table_as_dataset(conn, {'schema': 'refined', 'name': 'everyscore_patient'})
    df['mr_lods'] = df['lods'].apply(map_lods)    
    return df.loc[:, ['subject_id', 'mr_lods']]
   
def map_mortality_rate_to_icu_level(mortality_rate):    
    if 0 < mortality_rate < 0.33:
        return 'Level 1'
    elif 0.33 <= mortality_rate < 0.66:
        return 'Level 2'
    elif 0.66 <= mortality_rate < 0.99:
        return 'Level 3'
    else:
        return 'Unknown'


def generate_csv_file_name():
    data_dir = f"{os.getenv('ROOT_DIR')}\\data\\"
    for i in range(1, 10):        
        file_name = f"cached_dataset_{i}.csv"
        if not os.path.exists(data_dir + file_name):
            return file_name

def cache_database(df):
    name = generate_csv_file_name()
    df.to_csv(f'{os.getenv("ROOT_DIR")}\\data\\{name}.csv', index=False)             


def map_sapsii(score):
    logit = -7.7631 + 0.0737 * (score) + 0.9971 *  (np.log(score+1))
    return (np.exp(logit)) / (1 + np.exp(logit))

def map_lods(score):
     logit = -3.4043 + 0.4173 * (score)
     return (np.exp(logit)) / (1 + np.exp(logit))

def map_apsiii():
    pass

def map_oasis():
    pass

def weighted_average():
    pass

def average_mr():
    pass


# df['icu_level'] = df['mr_lods'].apply(map_mortality_to_icu_level)