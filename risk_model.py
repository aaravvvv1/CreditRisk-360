import pandas as pd
from sqlalchemy import create_engine

# 1. SETUP THE CONNECTION
# Format: postgresql+psycopg2://username:password@localhost:5432/database_name
# Note: Default postgres user is usually 'postgres'
# Replace your real password with a placeholder for the public code
db_connection_str = 'postgresql+psycopg2://postgres:YOUR_PASSWORD@localhost:5432/Financial_Risk_DB'
db_connection = create_engine(db_connection_str)

# 2. FETCH THE CLEAN DATA
# We use the clean table we verified in SQL earlier
query = "SELECT * FROM credit_risk_data"

print("Fetching data from PostgreSQL...")
df = pd.read_sql(query, db_connection)

# 3. VERIFY
print(f"Success! Loaded {len(df)} rows.")
print(df.head())