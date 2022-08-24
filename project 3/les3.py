import pandas as pd

melb_data = pd.read_csv("project 3\\data\\ufo.csv", sep=',')
melb_data.head()
melb_data['Time'] = pd.to_datetime(melb_data.Time)
print(melb_data['Time'].dt.year.mode()[0])

melb_data['Date'] = melb_data['Time'].dt.date
print(melb_data[melb_data['State']=='NV']['Date'].diff().dt.days.mean())