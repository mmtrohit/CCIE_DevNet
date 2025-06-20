import json
with open("sample.json","r") as stream:
    json_data = json.load(stream)
    print(type(json_data))
    print(json_data)
