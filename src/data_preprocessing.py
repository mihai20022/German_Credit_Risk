import pandas as pd

df = pd.read_csv('./data/raw/german_credit_data.csv')

print(df.head())

df.shape