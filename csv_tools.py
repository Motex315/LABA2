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