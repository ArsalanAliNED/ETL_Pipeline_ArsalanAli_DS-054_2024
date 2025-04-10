import pandas as pd
from pymongo import MongoClient

# Sample satellite data
data = {
    'Region': ['Punjab', 'Sindh', 'KPK', 'Balochistan'],
    'NDVI': [0.65, 0.70, 0.55, 0.60],
    'Soil_Moisture': [20.5, 22.1, 18.9, 21.3],
    'Date': pd.to_datetime(['2024-04-01', '2024-04-01', '2024-04-01', '2024-04-01'])
}

df = pd.DataFrame(data)

# Connect to MongoDB
client = MongoClient("mongodb+srv://aliali:aliali@cluster0.194dxnq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['agriculture']
collection = db['satellite_metrics']

# Insert data into MongoDB
collection.insert_many(df.to_dict('records'))

print("Satellite data inserted into MongoDB.")