table = 'books.csv'

def get_title(dataset):
    dataset.seek(0)
    title = next(dataset)
    title = title.split(';')
    title = [col.strip() for col in title]
    print(title)
    return title

def get_object(line, title):
    fields = []
    value = ''
    in_complex = False
    for char in line:
        if in_complex:
            value += char

            if char == '"':
                if value != '':
                    value = value[:-1]
                    fields.append(value)
                    value = ''
                    in_complex = False
        else:
            if char not in [';', '"']:
                value += char
                continue

            if char == ';':
                fields.append(value)
                value = ''
                continue

            if char == '"':
                in_complex = True
                continue

    return fields

with open(table) as dataset:
    title = get_title(dataset)
    i = 1
    outlist = []
    while i != 20:
        line = next(dataset)
        res = get_object(line,title)
        outlist.append(res[3]+'. '+res[1]+' - '+res[6][6:11])
        i+=1

outres = outlist[0]
for i in range(1,len(outlist)):
     outres = outres+'\n'+outlist[i]

with open("OUT_PATH", 'w') as out:
            out.write(str(outres))
