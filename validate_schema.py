import pandas as pd
import json

df = pd.read_csv('output/final_cleaned_data.csv')
with open('schema.json') as f:
    schema = json.load(f)

for col, dtype in schema['columns'].items():
    assert col in df.columns, f"{col} missing from CSV"
    assert str(df[col].dtype) == dtype, f"{col} has wrong dtype: {df[col].dtype} vs expected {dtype}"
