import pandas as pd
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. CONNECT & LOAD
# (Use your updated connection string from the last step)
# Replace your real password with a placeholder for the public code
db_connection_str = 'postgresql+psycopg2://postgres:YOUR_PASSWORD@localhost:5432/Financial_Risk_DB'
db_connection = create_engine(db_connection_str)

print("Loading data...")
df = pd.read_sql("SELECT * FROM credit_risk_data", db_connection)

# 2. PREPROCESSING
# Convert all text columns to numbers (One-Hot Encoding)
X = pd.get_dummies(df.drop('loan_status', axis=1), drop_first=True)
y = df['loan_status'] # This is what we want to predict (0 or 1)

# 3. SPLIT DATA (80% for training, 20% for testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. TRAIN THE MODEL
print("Training the Random Forest model... (this might take 10 seconds)")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. EVALUATE
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy:.2%}")

# 6. KEY INSIGHT: What matters most?
print("\nTop 5 Drivers of Default:")
feature_importance = pd.Series(model.feature_importances_, index=X.columns)
print(feature_importance.nlargest(5))