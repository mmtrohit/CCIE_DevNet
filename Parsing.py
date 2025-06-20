#import yaml
# with open("sample.yaml","r") as stream:
#     yaml_data=yaml.safe_load(stream)
#     print(type(yaml_data))
#     print(yaml_data)
#     print(yaml_data["People"][1]["Email"])


##### FROM JSON TO PYTHON PARSING ########

import json
# with open("sample.json","r") as file:
#     json_file=json.load(file)
#     print(json_file)
#     print(type(json_file))

# a={'People': [{'Id': '1', 'FirstName': 'Rohit', 'LastName': 'Dwivedi', 'Email': 'ciscosoni1@gmail.com'}, {'Id': '2', 'FirstName': 'Ankush', 'LastName': 'Sharma', 'Email': 'johnpaul1@gmail.com'}, {'Id': '3', 'FirstName': 'Ben', 'LastName': 'Mark', 'Email': 'benmark1@gmail.com'}]}
#
#
# with open("new_json1.json","a") as file:
#     json.dump(a,file)
#     print("FILE IS SUCCESSFULY COPIED")




#######XML to PYTHON PARSING############

#
# import xml.etree.ElementTree as ET
#
# with open("new1234.xml", "r") as file:
#     xml=ET.parse(file)
#     print(xml)
#
#     for i in xml.iter():
#         print(i.tag + ":" + i.text)





