# import yaml
# with open ("sample.yaml","r") as stream:
#     user_yaml=yaml.safe_load(stream)
#     print(user_yaml)
#     print(user_yaml["People"][1]["FirstName"])
from multiprocessing.context import ProcessError

# import yaml
# with open ("sample.yaml","r") as stream:
#     user_yaml=yaml.safe_load(stream)
#     print(user_yaml["People"][0]["Email"])

d={'People': [{'Id': '1', 'FirstName': 'Suraj', 'LastName': 'Soni', 'Email': 'ciscosoni1@gmail.com'}, {'Id': '2', 'FirstName': 'John', 'LastName': 'Paul', 'Email': 'johnpaul1@gmail.com'}, {'Id': '3', 'FirstName': 'Ben', 'LastName': 'Mark', 'Email': 'benmark1@gmail.com'}]}


# import json
# # with open("sample.json","r") as file:
# #     json_obj=json.load(file)
# #     print(json_obj)
#
#
# with open("Python_to_Json.json","a+") as file:
#     json.dump(d,file)

import xml.etree.ElementTree as ET
with open("sample.xml","r") as file:
    xml=ET.parse(file)
    root=xml.getroot()

print("PRINTING THE XML TAG AND VALUE")

for row in root.iter():
    print(row.tag + ":" + row.text)
