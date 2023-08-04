from preprocessing import run_preprocessing_pipeline, load_data

df = load_data()
df = run_preprocessing_pipeline(df)

