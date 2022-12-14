import pandas as pd
melb_data = pd.read_csv('project 2\data\melb_data.csv', sep=',')
melb_data['Car'] = melb_data['Car'].astype('int64')
melb_data['Bedroom'] = melb_data['Bedroom'].astype('int64')
melb_data['Bathroom'] = melb_data['Bathroom'].astype('int64')
melb_data['Propertycount'] = melb_data['Propertycount'].astype('int64')
melb_data['YearBuilt'] = melb_data['YearBuilt'].astype('int64')
#print(melb_data[(melb_data['SellerG'] == 'Nelson') & (melb_data['Price'] > 3000000)])
#print(melb_data[melb_data['BuildingArea'] == 0]['Price'].min())
#print(round(melb_data[(melb_data['Price']<1e6) & ((melb_data['Rooms']>5) | (melb_data['YearBuilt'] > 2015))]['Price'].mean()))
print(melb_data[(melb_data['Type'] == 'h') & (melb_data['Price'] < 3000000)]['Regionname'].mode())