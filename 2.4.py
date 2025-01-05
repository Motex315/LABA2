import xml.dom.minidom as minidom


xml_file = open('currency.xml', 'r')
xml_data = xml_file.read()

dom = minidom.parseString(xml_data)
dom.normalize()

elements = dom.getElementsByTagName('Valute')
num_list = []
char_list = []

for node in elements:
    for child in node.childNodes:
        if child.nodeType == 1:
            if child.tagName == 'NumCode':
                if child.firstChild.nodeType == 3:
                    num_list.append(int(child.firstChild.data))
            if child.tagName == 'CharCode':
                if child.firstChild.nodeType == 3:
                    char_list.append(str(child.firstChild.data))

print(num_list)
print(char_list)