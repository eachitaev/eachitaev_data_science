from operator import index
from statistics import median
import pandas as pd

melb_df = pd.read_csv('project 4\data\melb_data_fe.csv')
melb_df['Date'] = pd.to_datetime(melb_df['Date'], dayfirst=True)
print(melb_df.pivot_table(values='BuildingArea',index='Type',columns='Rooms', aggfunc=median))
pivot = melb_df.pivot_table(
    values='Price',
    index='SellerG',
    columns='Type',
    aggfunc='median',
)
max_unit_price = pivot['unit'].max()
print(pivot[pivot['unit'] == max_unit_price].index[0])