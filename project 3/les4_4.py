import pandas as pd

def get_experience(arg):
    """
    Напишите функцию get_experience(arg), аргументом которой является строка столбца с опытом работы. 
    Функция должна возвращать опыт работы в месяцах. Не забудьте привести результат к целому числу.
    """
    arg_month = ['месяц','месяцев','месяца']
    arg_year = ['лет', 'год', 'года']
    arg_exp = arg.split(' ')
    month = 0
    year = 0
    for i in range(len(arg_exp)):
        if arg_exp[i] in arg_year:
            year = 12 * int(arg_exp[i-1])
        if arg_exp[i] in arg_month:
            month = int(arg_exp[i-1])
    return year + month


if __name__ == '__main__':
    experience_col = pd.Series([
        'Опыт работы 8 лет 3 месяца',
        'Опыт работы 3 года 5 месяцев',
        'Опыт работы 1 год 9 месяцев',
        'Опыт работы 3 месяца',
        'Опыт работы 6 лет'
        ])
    experience_month = experience_col.apply(get_experience)
    print(experience_month)