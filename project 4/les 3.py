from operator import index
import pandas as pd

melb_df = pd.read_csv('project 4\data\melb_data_fe.csv')
melb_df['Date'] = pd.to_datetime(melb_df['Date'], dayfirst=True)
print(melb_df.groupby(by='Rooms')['Price'].mean().sort_values(ascending=False))
print(melb_df.groupby('Regionname')['Lattitude'].std().sort_values())
date1 = pd.to_datetime('2017-05-01')
date2 = pd.to_datetime('2017-09-01')
mask = (date1 <= melb_df['Date']) & (melb_df['Date']<= date2)
print(melb_df[mask].groupby('SellerG')['Price'].sum().sort_values(ascending=True))