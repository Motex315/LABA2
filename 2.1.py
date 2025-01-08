from csv_tools import get_title, get_object

table = 'books.csv'

with open(table) as dataset:
    title = get_title(dataset)
    i = 0
    try:
        while next(dataset) != '':
            line = next(dataset)
            res = get_object(line,title)
            if len(res[1]) > 30:
                i+=1
    except:
        pass
    
print(i)