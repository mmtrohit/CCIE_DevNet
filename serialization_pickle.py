#import pickle


friends= {"Dan": [20,"London",12345], "Maria": [25,"Marid",3445156]}
#friends2= {"Alpha": [20,"Manchaster",1345], "Romio": [25,"Marid",34456]}
#new_friends=(friends1,friends2)

#with open("friends.dat","wb") as f:
 #   pickle.dump(new_friends,f)


#with open("friends.dat","rb") as f:
 #   obj=pickle.load(f)
  #  print(type(obj))
  #  print(obj)

"""import json
with open ("nfriends.json","w") as f:
    x=json.dump(friends,f,indent=4)
    print(type(x))


with open ("friends.json","w") as f:
     a=json.dumps(friends,indent=4)
     print(a)
     print(type(a)) """

"""import json
with open("nfriends.json","rt") as f:
    obj=json.load(f)
    print(obj)
    print(type(obj)) """

"""jason_string=json.dumps(friends)
print(jason_string)
print(type(jason_string)) """

import json
friends= {"Dan": (20,"London",12345), "Maria": (25,"Marid",3445156)}

with open("nfriends.json") as f:
    obj=json.load(f)
    print(type(obj))
    print(obj)

json_string = """{
    "Dan": [
        20,
        "London",
        12345
    ],
    "Maria": [
        25,
        "Marid",
        3445156
    ]
}"""

obj=json.loads(json_string)
print(type(obj))
print(obj)

