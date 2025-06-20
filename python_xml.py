# import xmltodict
# with open("sample.xml","r") as stream:
#     xml=xmltodict.parse(stream.read())
#     print(type(xml))
#     print(xml)

# import xml.etree.ElementTree as ET
#
# with open("sample.xml","r") as stream:
#     xml=ET.parse(stream)
#     root=xml.getroot()
#     print(root)
#
#     for row in root.iter():
#         print(row.tag + ":" + row.text)