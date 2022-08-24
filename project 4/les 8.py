import pandas as pd
import re 


def get_year_release(arg):
    #находим все слова по шаблону "(DDDD)"
    candidates = re.findall(r'\(\d{4}\)', arg) 
    # проверяем число вхождений
    if len(candidates) > 0:
        #если число вхождений больше 0,
	#очищаем строку от знаков "(" и ")"
        year = candidates[0].replace('(', '')
        year = year.replace(')', '')
        return int(year)
    else:
        #если год не указан, возвращаем None
        return None

#1
ratings = pd.read_csv('project 4\data\\ratings_movies.csv')
ratings['year_release'] = ratings['title'].apply(get_year_release)
ratings.info()

#2
print(ratings[ratings['year_release']== 1999].groupby('title')['rating'].mean().sort_values())

#3
print(ratings[ratings['year_release']== 2010].groupby('genres')['rating'].mean().sort_values())

#4
print(ratings.groupby('userId')['genres'].nunique().sort_values(ascending=False))

#5
print(ratings.groupby('userId')['rating'].agg(
    ['count', 'mean']
).sort_values(['count', 'mean'], ascending=[True, False]))

#6
new_ratings = ratings[ratings['year_release']== 2018].groupby('genres')['rating'].agg(
    ['mean', 'count'])
print(new_ratings[new_ratings['count']>10].sort_values(['mean'], ascending=[False]))

#7
ratings['date'] = pd.to_datetime(ratings['date'])
ratings['year_rating'] = ratings['date'].dt.year
pivot = ratings.pivot_table(
    index='year_rating',
    columns='genres',
    values='rating',
    aggfunc='mean'
)
print(pivot)

###########################################
products = pd.read_csv('project 4\data\products.csv', sep=';')
orders = pd.read_csv('project 4\data\orders.csv', sep=';')
print(products)
print(orders)

#8
orders_products = orders.merge(
    products, 
    left_on='ID товара',
    right_on='Product_ID',
    how='left')
print(orders_products)

#9
print(orders_products[orders_products['Отменен'] == 'Да']['Name'])

#10
orders_products['Profit'] = orders_products['Price'] * orders_products['Количество'] 
print(orders_products[orders_products['Оплачен'] == 'Да'].groupby('ID Покупателя')['Profit'].sum().sort_values(ascending=False))