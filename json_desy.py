import json
with open("ourfriends.json","r") as f:
    obj=json.loads(f)
    print(type(obj))
    print(obj)