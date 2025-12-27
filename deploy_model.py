import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sklearn.ensemble import RandomForestClassifier

# 1. CONNECT
# (Use your CORRECTED password and database name here)
# Replace your real password with a placeholder for the public code
db_connection_str = 'postgresql+psycopg2://postgres:YOUR_PASSWORD@localhost:5432/Financial_Risk_DB'
db_connection = create_engine(db_connection_str)

print("Loading full dataset...")
df = pd.read_sql("SELECT * FROM credit_risk_data", db_connection)

# 2. PREPARE DATA
# We need to encode the data exactly like we did for training
X = pd.get_dummies(df.drop('loan_status', axis=1), drop_first=True)

# 3. TRAIN FINAL MODEL (On All Data)
print("Training final production model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, df['loan_status'])

# 4. PREDICT PROBABILITIES
# This gives us the % chance of default (e.g., 0.85 = 85% chance)
probs = model.predict_proba(X)[:, 1]

# 5. CREATE NEW COLUMNS
df['probability_of_default'] = np.round(probs, 4)

# Create Risk Tiers logic
conditions = [
    (df['probability_of_default'] < 0.20),
    (df['probability_of_default'] >= 0.20) & (df['probability_of_default'] < 0.60),
    (df['probability_of_default'] >= 0.60)
]
choices = ['Low Risk', 'Medium Risk', 'High Risk']
df['risk_segment'] = np.select(conditions, choices, default='Critical')

# 6. EXPORT TO CSV FOR POWER BI
print("Exporting to 'risk_scored_data.csv'...")
df.to_csv(r'C:\Users\aarav\Desktop\Credit Risk\risk_scored_data.csv', index=False)

print("DONE! Your data is ready for Power BI.")
print(df[['person_income', 'probability_of_default', 'risk_segment']].head())