import pandas as pd

c_t = pd.read_csv('project 3\data\citibike-tripdata.csv', sep=',')
ct = c_t.copy()
mode_usertype = c_t['usertype'].mode()[0]
print(mode_usertype)
count_mode_user = c_t[c_t['usertype'] == mode_usertype].shape[0]
print(round(count_mode_user / c_t.shape[0], 2))
#print(c_t.info())
#print(c_t(c_t['usertype'] == 'Subscriber'))
mode_usertype = c_t['gender'].mode()[0]
#print(mode_usertype)
count_male_user = c_t[c_t['gender'] == mode_usertype].shape[0]
#print(count_male_user)
#print(c_t['birth year'].max())
#print(c_t['start station name'].describe)
ct.drop(['start station id','end station id'],axis=1,inplace=True)
ct['age'] = 2018 - ct['birth year']
ct.drop(['birth year'], axis=1, inplace=True)
print(ct[ct['age'] > 60].shape[0])
ct['trip duration'] =  pd.to_datetime(ct['stoptime']) - pd.to_datetime(ct['starttime'])
print(ct['trip duration'].mean().seconds)
weekday = pd.to_datetime(ct['starttime']).dt.dayofweek
#print(weekday)
ct['weekend'] = weekday.apply(lambda x: 1 if x ==5 or x == 6 else 0)
print(ct['weekend'].sum())

def get_time_of_day(time):
    if 0 <= time <= 6:
        return 'night'
    elif 6 < time <= 12:
        return 'morning'
    elif 12 < time <= 18:
        return 'day'
    elif 18 < time <= 23:
        return 'evening'
    else:
        return 'else'


ct['time_of_day'] = pd.to_datetime(ct['starttime']).dt.hour.apply(get_time_of_day)
a = ct[ct['time_of_day'] == 'day'].shape[0]
b = ct[ct['time_of_day'] == 'night'].shape[0]
print(round(a / b))