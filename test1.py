import json
with open ("ourfriends.json", "rt") as f:
    obj=json.loads(f)
# friends1= {"Vishal":(20,"Delhi",12445), "Abhay":(24,"noida",595959)}
    print(obj)
