from operator import index
import pandas as pd

melb_df = pd.read_csv('project 4\data\melb_data_fe.csv')
melb_df['Date'] = pd.to_datetime(melb_df['Date'], dayfirst=True)
print(melb_df.sort_values(by='AreaRatio', ignore_index=True).iloc[1558])
print(melb_df.sort_values(by='AreaRatio', ignore_index=True, ascending=False).loc[1558])
print(int(melb_df.sort_values(
    by='AreaRatio', 
    ignore_index=True,
    ascending=False
).loc[1558, 'BuildingArea']))
mask1 = melb_df['Type'] == 'townhouse'
mask2 = melb_df['Rooms'] > 2
print(int(melb_df[mask1&mask2].sort_values(
    by=['Rooms', 'MeanRoomsSquare'],
    ascending=[True, False],
    ignore_index=True
).loc[18, 'Price'])
)