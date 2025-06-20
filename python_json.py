import json

a= {'People': [{'Id': '1', 'FirstName': 'Suraj', 'LastName': 'Soni', 'Email': 'ciscosoni1@gmail.com'}, {'Id': '2', 'FirstName': 'John', 'LastName': 'Paul', 'Email': 'johnpaul1@gmail.com'}, {'Id': '3', 'FirstName': 'Ben', 'LastName': 'Mark', 'Email': 'benmark1@gmail.com'}]}

# with open("user.json","a") as file:
#     json.dump(a,file)
#
# with open ("user.json","r") as file:
#     new_file=json.load(file)
#     print(new_file)

with open("new_file1.json","w") as file:
    json.dump(a,file,indent=4)



import requests
test= requests.post()
