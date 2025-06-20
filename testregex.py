import re
with open("show_version.txt") as file:
    ver_output=file.read()
#   print(ver_output)


my_pattern=re.compile(r"(cisco)\.(\w+)")
result=my_pattern.search(string=ver_output)

my_pattern=re.compile(r"C....")
result1=my_pattern.finditer(string=ver_output)
print(result1)
#help(my_pattern.finditer)
#print(len(result1))
for res in result1:
 #   print(res.group(1)



#####################################

 "Validate User input"
input1=input("Enter python version : ")
my_pattern=re.compile(r"python3(\.\d+)?")
match=my_pattern.search(input1)
if match:
    print(f"input matched with{input1}")
else:
    print("not matched ")