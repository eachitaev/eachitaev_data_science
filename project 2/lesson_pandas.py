import re
import pandas as pd

def create_medications(names, counts):
    """
    Напишите функцию create_mediactions(names, counts), которая  создает Series medications,
    индексами которой являются названия лекарств names, а значениями - их количество в поставке counts
    """
    return pd.Series(data=counts,index=names)

   

def get_percent(medications, name):
    """
    А также напишите функцию get_percent(medications, name), которая возвращает долю количества товара
    с именем name от общего количества товаров в поставке в процентах.
    """
    return medications[name]/sum(medications)*100


if __name__ == '__main__':
    names=['chlorhexidine', 'cyntomycin', 'afobazol']
    counts=[15, 18, 7]
    medications = create_medications(names, counts)
    print(get_percent(medications, "chlorhexidine")) #37.5