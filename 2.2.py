import csv

table = 'books.csv'

def get_title(dataset):
    dataset.seek(0)
    title = next(dataset)
    title = title.split(';')
    title = [col.strip() for col in title]
    print(title)
    return title

def filter_ath_200(dataset, title, athor_inp):
    filtered = []

    for line in dataset:
        obj = get_object(line, title)
        athor = obj['Автор (ФИО)']
        price = obj['Цена поступления']
        if athor == athor_inp:
            if float(price) >= 200:
                filtered.append(obj)

    dataset.seek(0)
    return filtered

def get_object(line, title):
    reader = csv.DictReader([line], title, delimiter=';', quotechar='"')
    res = next(reader)
    return res

with open(table) as dataset:
    title = get_title(dataset)
    res = filter_ath_200(dataset, title, input())
    line = next(dataset)
print(res)