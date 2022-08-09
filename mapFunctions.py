def to_icu_level(df):
    icu_level = []
    for index, row in df.iterrows():
        if(row["avrg_mr"] > 0 and row["avrg_mr"] <= 0.33):
            icu_level.append(1)
        elif(row["avrg_mr"] > 0.33 and row["avrg_mr"] <= 0.66):
            icu_level.append(2)
        else:
            icu_level.append(3)
    df["icu_level"] = icu_level
    return df

def to_avrg_mr(df):
    avrg_mr = []
    for index, row in df.iterrows():
        lodsmr = lods_to_mr(row['lods'])
        sapsmr = sapsii_to_mr(row['sapsii'])
        avrg_mr.append((lodsmr + sapsmr) / 2)
    df["avrg_mr"] = avrg_mr
    return df

def sapsii_to_mr(sapsii):
    logit = -7.7631 + (0.0737 * sapsii) + (0.9971 * np.log(sapsii + 1))
    return (np.exp(logit)) / (1 + np.exp(logit))

def lods_to_mr(lods):
    logit = -3.4043 + 0.4173 * (lods)
    return (np.exp(logit) / (1 + np.exp(logit)))

def apache_to_mr(score):
    logit = -3.517 + (0.146 * score)
    return (np.exp(logit)) / (1 + np.exp(logit))

def to_icu_level(df):
    df_fpmExternalValidation["icu_level"] = ""
    for i, row in df.iterrows():
        if(row["avrg_mr"] > 0 and row["avrg_mr"] <= 0.33):
            df_fpmExternalValidation.at[i, "icu_level"] = 1
        elif(row["avrg_mr"] > 0.33 and row["avrg_mr"] <= 0.66):
            df_fpmExternalValidation.at[i, "icu_level"] = 2
        else:
            df_fpmExternalValidation.at[i, "icu_level"] = 3
    return df