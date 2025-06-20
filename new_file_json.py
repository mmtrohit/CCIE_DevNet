import json

import xmltodict

from lab1_inventory import *

### Python to Json####

"""with open("newtest.json","w") as file :
    json.dump(inventory_list,file,indent=4) """

#######USING DUMPS####################

"""with open("newtest1.json","w") as file:
    st= json.dumps(inventory_dict,indent=4)
    file.write(st) """

##########using Load ###############


"""with open("newtest.json") as file:
    output=file.read()
    print(output)"""


"""with open("newtest.json") as file:
    test=json.load(file)
    print(test)
    print(type(test))"""


##############CONVERTING A PYTHON FILE TO YAML############

import yaml
from pprint import pprint

"""with open("newtest32.yaml","w") as file:
    file.write(yaml.dump(inventory_list)) """

"""with open("newtest32.yaml") as file:
    x=yaml.safe_load(file)
    pprint(x)
    print(type(x))"""

###############PYTHON TO XML##################

import xmltodict
from pprint import pprint
"""with open("new1234.xml") as file:
    output=xmltodict.parse(file.read())
    pprint(output["inventory"]["device"][1]["username"])"""

"""with open("new1234.xml") as file:
    output=xmltodict.parse(file.read(),dict_constructor=dict)
    pprint(output)"""

##########USING ELEMENT TREE##############

"""import xml.etree.ElementTree as ET
tree=ET.parse("all_int.xml")
root=tree.getroot()
print(root[0][0][0][0][1][0][0][1].text)"""
