import pandas as pd
melb_data = pd.read_csv('project 2\data\melb_data.csv', sep=',')
print(melb_data.loc[3521,'Landsize']/melb_data.loc[1690,'Landsize'])
print(melb_data.info())