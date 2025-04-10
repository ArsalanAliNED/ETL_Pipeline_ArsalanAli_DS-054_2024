import pandas as pd

def test_yield_positive():
    df = pd.read_csv('output/final_cleaned_data.csv')
    assert (df['Yield'] > 0).all()

def test_profitability_exists():
    df = pd.read_csv('output/final_cleaned_data.csv')
    assert 'Profitability' in df.columns
