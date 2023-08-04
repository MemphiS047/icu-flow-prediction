from preprocessing import run_preprocessing_pipeline, load_data
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Loading data and preprocessing
print("Loading data and preprocessing...")
df = load_data()
df = run_preprocessing_pipeline(df)

# Lable Encoding
# print("Lable encoding...")
# label_encoder = LabelEncoder()
# df["icu_level"] = label_encoder.fit_transform(df["icu_level"])

# Scaling data
# print("Scaling data...")
# scaler = StandardScaler()
# df = scaler.fit_transform(df)