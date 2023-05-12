import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.model_selection import train_test_split

# Load the data
data = pd.read_csv('data.csv')  # Replace 'data.csv' with your data file

# Separate features and target variable
X = data.drop('target', axis=1)  # Replace 'target' with your target column name
y = data['target']

# Perform train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  # Adjust test_size and random_state as needed

# Preprocessing steps for numerical features
numerical_features = ['numerical_col1', 'numerical_col2']  # Replace with your numerical feature column names

scaler = StandardScaler()
X_train[numerical_features] = scaler.fit_transform(X_train[numerical_features])
X_test[numerical_features] = scaler.transform(X_test[numerical_features])

# Preprocessing steps for categorical features
categorical_features = ['categorical_col1', 'categorical_col2']  # Replace with your categorical feature column names

label_encoder = LabelEncoder()
for feature in categorical_features:
    X_train[feature] = label_encoder.fit_transform(X_train[feature].astype(str))
    X_test[feature] = label_encoder.transform(X_test[feature].astype(str))

# Preprocessing steps for text features
text_features = ['text_col1', 'text_col2']  # Replace with your text feature column names

tfidf_vectorizer = TfidfVectorizer()
X_train_text = tfidf_vectorizer.fit_transform(X_train[text_features].astype(str))
X_test_text = tfidf_vectorizer.transform(X_test[text_features].astype(str))

# Preprocessing steps for feature selection (optional)
k = 10  # Specify the number of top features to select

selector = SelectKBest(chi2, k=k)
X_train_selected = selector.fit_transform(X_train, y_train)
X_test_selected = selector.transform(X_test)

# Merge preprocessed features
X_train_processed = pd.concat([X_train_selected, pd.DataFrame(X_train_text.toarray())], axis=1)
X_test_processed = pd.concat([X_test_selected, pd.DataFrame(X_test_text.toarray())], axis=1)

# Training and evaluation with a machine learning model
from sklearn.ensemble import RandomForestClassifier  # Replace with your desired model

model = RandomForestClassifier()
model.fit(X_train_processed, y_train)
accuracy = model.score(X_test_processed, y_test)

print("Accuracy:", accuracy)
