import json

from urllib3.connection import port_by_scheme

import requests
#d={"name":"Rohit"}

"""response= requests.get("https://jsonplaceholder.typicode.com/todos")
todos=json.loads(response.text)
print(type(todos))
print(todos)
for task in todos:
    if task["completed"]== True:
        print(task) """


#post=requests.post("https://jsonplaceholder.typicode.com/todos")
#todos=json.dumps(d)


##################CHALLANGE CODE################

"""import requests
import json
response=requests.get("https://jsonplaceholder.typicode.com/users")
todos=json.loads(response.text)
print(todos)


for i in todos:
    print(i["name"])
    print(["name"]["address"])"""
  #  print(x["city"])
  #  print(x["geo"]) """



#################################### Serialization and deSerialization of file###########

"""def ser(obj,file,type):
    if type=="pickle":
        import pickle
        with open(obj,"wb") as f:
            pickle.dump(obj,f)


d1 = {'a': 'x', 'b': 'y', 'c': 'z', 30: (2, 3, 'a')}

# Serializing using pickle
ser(d1, 'a.dat', 'pickle')"""

