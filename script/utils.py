# Returns columns without mean columns (e.g. 'column_min', 'column_max') and missing mean columns (e.g. 'column_mean').
def detect_missing_mean_columns(df):
    missing_mean_cols = []
    for column in df.columns:
        if '_min' in column and column.replace('_min', '_max') in df.columns:
            mean_column = column.replace('_min', '_mean')
            if mean_column not in df.columns:
                missing_mean_cols.append((column, mean_column))
    return missing_mean_cols

# Calculates mean values
def calculate_mean(row, min_col, max_col):
    return (row[min_col] + row[max_col]) / 2

# Adds missing mean columns to the dataframe given the returned list of mean columns
def add_missing_mean_columns(df, missing_mean_cols):
    for min_col, mean_col in missing_mean_cols:
        df[mean_col] = df.apply(lambda row: calculate_mean(row, min_col, min_col.replace('_min', '_max')), axis=1)
    return df

# Removes min and max columns
def remove_min_max_columns(df):
    mean_columns = [col for col in df.columns if '_mean' in col]
    df = df[mean_columns]
    return df