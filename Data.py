####### Data Serilization in Python

"""import pickle
friends1={"Vishal":[20,"Delhi",12445], "Abhay":[24,"noida",595959]}
friends2={"Rahul":[20,"New_Delhi",12445], "Akshay":[24,"BNGLR",595959]}
friends=(friends1,friends2)
with open("ourfriends.dat","wb") as f:
    pickle.dump(friends,f)

with open("ourfriends.dat","rb") as f:
    obj=pickle.load(f)
    print(obj)
    print(type(obj)) """


import json
from sys import intern

friends1={"Vishal":[20,"Delhi",12445], "Abhay":[24,"noida",595959]}

"""with open("ourfriends.json","w") as f:
    json.dump(friends1,f,indent=4)


new_obj=json.dumps(friends1, indent= 4)
print(type(new_obj))
print(new_obj)


json_string = """{
    "Vishal":(
        20,
        "Delhi",
        12445
    ),
    "Abhay":(
        24,
        "noida",
        595959
    )
} """

obj=json.loads(json_string)
print(obj)
print(type(obj)) """


new_friends1={"Vishal":(20,"Delhi",12445), "Abhay":(24,"noida",595959)}
obj=json.load(new_friends1)
print(obj)