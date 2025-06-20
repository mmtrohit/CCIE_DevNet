import json
from textwrap import indent

from lab_inventory import *
from lib_netmiko_scp import new_inventory

"""with open("lab_inventory.json","w") as file:
    file.write(json.dumps(inventory_dict, indent=4)) """

"""with open("lab_inventory.json") as file:
    output=json.load(file)
    print(type(output))
    print(output) """

"""with open("lab_inventory.json","w") as file:
    st=json.dumps(inventory_dict,indent=4)
    print(st) """

#with open("new_lab_inventory.json","w") as file:
#   file.write(json.dumps(inventory_list,indent=4))

################PY_FILE TO JSON_FILE###########(load)####
#from new_user import *

"""with open("new_user.json","w") as file:
    json.dump(new_inventory,file,indent=4) """

#with open("new_user.json") as test:

 #   output=json.load(test)
 #   print(output)


#with open("new_user.json") as file:
#    output=file.read()

#new_output=json.loads(output)


"""with open("test_file.json","w") as file:
    new = json.dumps(new_inventory, indent=4)
    file.write(new)"""



"""with open("new1test.json","w") as file:
    json.dump(new_inventory,file, indent=4)"""

#readJSON FILE TO PYTHON
#with open("new_user.json") as file:
 #   x=json.load(file)
 #   print(x)


 #Using Loads

#with open("new_user.json") as file:
#    st=file.read()
##    print(st)


#new_file=json.dumps(st)
#print(new_file)


#with open("test1234.json","w") as file:
 #   json.dump(inventory_list,file, indent=4)


"""with open("test12344.json","w") as file:
    st=json.dumps(inventory_list,indent=4)
    file.write(st)"""


import yaml
from pprint import pprint
"""with open("file1.yaml") as file:
    output=yaml.safe_load(file)
    print(output)"""

"""with open("new_file.yaml","w") as file:
    file.write(yaml.dump(new_inventory))"""


import xmltodict

#PYTHON TO XML

#with open("New_file.xml","w") as file:
 #   file.write(xmltodict.unparse(inventory_dict ,pretty=True))


#with open("py1_to_xml.xml") as file:
#    new=xmltodict.parse(file.read(),dict_constructor=dict)
#    pprint(new)

"""with open("all_int.xml") as file:
    output=xmltodict.parse(file.read(), dict_constructor=dict)
    print(output)"""

"""x=output['rpc-reply']
pprint(x)"""

import xml.etree.ElementTree as ET
tree=ET.parse("all_int.xml")
root=tree.getroot()
print(root[0][0][0][0][0].text)