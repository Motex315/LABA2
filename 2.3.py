from csv_tools import get_title, get_object

table = 'books.csv'
OUT_PATH = 'out3.txt'


with open(table) as dataset:
    title = get_title(dataset)
    i = 1
    outlist = []
    while i != 20:
        line = next(dataset)
        res = get_object(line,title)
        author = res[3]
        title = res[1]
        year = res[6][6:11]
        link = f'{author}. {title} - {year}'
        outlist.append(link)
        i+=1

outres = outlist[0]
for i in range(1,len(outlist)):
     outres = outres+'\n'+outlist[i]

with open(OUT_PATH, 'w') as out:
            out.write(str(outres))
