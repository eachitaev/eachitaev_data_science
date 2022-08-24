import pandas as pd

melb_data = pd.read_csv('project 3\data\melb_data_ps.csv', sep=',')
melb_data.head()
melb_df = melb_data.copy()
melb_df.head()
melb_df.drop(['index','Coordinates'],axis=1,inplace=True)
melb_df.head()
total_rooms = melb_df['Rooms'] + melb_df['Bedroom'] + melb_df['Bathroom']
melb_df['MeanRoomsSquare'] = melb_df['BuildingArea'] / total_rooms
diff_area = melb_df['BuildingArea'] - melb_df['Landsize']
sum_area = melb_df['BuildingArea'] + melb_df['Landsize']
melb_df['AreaRatio'] = diff_area/sum_area
print(melb_df['AreaRatio'])

countries_df = pd.DataFrame({
    'country': ['Англия', 'Канада', 'США', 'Россия', 'Украина', 'Беларусь', 'Казахстан'],
    'population': [56.29, 38.05, 322.28, 146.24, 45.5, 9.5, 17.04],
    'square': [133396, 9984670, 9826630, 17125191, 603628, 207600, 2724902]
})

def get_weekend(weekday):
    if weekday == 5 or weekday == 6:
        return 1
    else: 
        return 0


melb_df['Date'] = pd.to_datetime(melb_df['Date'], dayfirst=True)
melb_df['WeekdaySale'] = melb_df['Date'].dt.dayofweek
weekend_count = melb_df[(melb_df['WeekdaySale'] == 5) | (melb_df['WeekdaySale'] == 6)].shape[0]
print(weekend_count)
melb_df['Weekend'] = melb_df['WeekdaySale'].apply(get_weekend)
print(round(melb_df[melb_df['Weekend']==1]['Price'].mean()))

popular_seler = melb_df['SellerG'].value_counts().nlargest(49).index
# заменяем значения улиц, не попавших в список популярных на строку 'other'
melb_df['SellerG'] = melb_df['SellerG'].apply(lambda x: x if x in popular_seler else 'other') 

a = melb_df[melb_df['SellerG'] == 'Nelson']['Price'].min() 
b = melb_df[melb_df['SellerG'] == 'other']['Price'].min() 
print(round(a/b, 1))