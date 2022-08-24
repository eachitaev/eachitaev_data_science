import pandas as pd

melb_df = pd.read_csv('project 4\data\melb_data_fe.csv')
melb_df['Date'] = pd.to_datetime(melb_df['Date'], dayfirst=True)
def get_time_of_day(time):
    if 1 <= time <= 3:
        return 1
    elif 3 < time <= 6:
        return 2
    elif 6 < time <= 9:
        return 3
    elif 9 < time <= 12:
        return 4
    else:
        return 5


melb_df['quarter'] = melb_df['MonthSale'].apply(get_time_of_day)
#print(melb_df.info())
#print(melb_df['quarter'])
#melb_df.iloc()
#print(melb_df['quarter'].value_counts())
cols_to_exclude = ['Date', 'Rooms', 'Bedroom', 'Bathroom', 'Car'] 
max_unique_count = 150 
for col in melb_df.columns: 
    if melb_df[col].nunique() < max_unique_count and col not in cols_to_exclude: 
        melb_df[col] = melb_df[col].astype('category')
print(melb_df.info())