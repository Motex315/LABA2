import xml.dom.minidom as minidom


xml_file = open('currency.xml', 'r')
xml_data = xml_file.read()

dom = minidom.parseString(xml_data)
dom.normalize()

elements = dom.getElementsByTagName('Valute')
NumList = []
CharList = []

for node in elements:
    for child in node.childNodes:
        if child.nodeType == 1:
            if child.tagName == 'NumCode':
                if child.firstChild.nodeType == 3:
                    NumList.append(int(child.firstChild.data))
            if child.tagName == 'CharCode':
                if child.firstChild.nodeType == 3:
                    CharList.append(str(child.firstChild.data))

print(NumList)
print(CharList)