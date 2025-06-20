"""Stu ={}

for i in range(2):
    name = input("Enter the Students name")
    Roll_no= int(input("Enter the Student Roll Number"))

    Stu[name]={"Roll_nu": Roll_no, "Profile": name}


print(Stu) """
import time
from multiprocessing.context import ProcessError
from selectors import SelectSelector

"""def addition( item,L =[ ]):
    L.append(item)
    return L

print(addition(5,[1,2,3,4]))
print(addition(55))
print(addition(65))
print(addition(75)) """


# num=2
"""for i in range(1,11):
   # x=i*num
  #  print(x,end=",")
    if i% 2==0:
        print("This is an even Number",i)

    else:
        print(i)
print() """


"""def add(a,b, /, c,d,e,f):
    return a+b+c+d+e+f

r= add(1,5,7,8,9,10)
print(r) """


"""def fun(**n):
    print(n)
    

fun(a=10,b=30) """


"""def days():
    L=["Sun","Mon","Tue","Wed","Thr","Fri","Sat"]
    i = 0
    while True:
        x=L[i]
        i=i+1
        print(i+1) %7 
        yield x

d=days()
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d)) """


"""x=input(("Enter the String"))
count=0
list=[]
while True:
    for row in x:
#        list.append(row)
        if row not in list:
            list.append(row)
        elif row in list:
            count=count+1
            print(("The Number of times{}").format(row),count)



 ##           count=count+1
##            list.append(row)
 ##           print(list)
  ##          print("Number if time it has",count)
        else:
            pass


    break

print(count) """

################## Recursion Program in Python #################

"""def num(n):
    if n==0:
        return 1
    else:
        return n* num(n-1)


print(num(5)) """




"""def diff(n1 , n2):
    if abs(n1-n2) <= 5:
        return True
    else:
        return False

print(diff(25,15)) """


"""def max(n1,n2,n3):
    if n1>n2:
        return n1
    elif n2>n3:
        return n2
    else:
        return n3


x=max(5,3,3)
print(x) """

"""def message(name,prof,/):
    print(("My name is {} amd I am an {}").format(name,prof))


message("Rohit", " Nothing")"""


"""def revert(d):
    newd={}
    for key,value in d.items():
        newd[value]=key
    return newd

d1= revert({"a" : 10, "b":20})
print(d1)"""


#u=0
#l=0

"""def cal(str):
    u=0
    l=0
    for i in str:
        if i.isupper():
            u=u+1
        elif i.islower():
            l=l+1
        #else:
            #continue


    return u,l


print(cal("ahahHAHAh")) """


"""def mini(*args,low_limit=None):
    print(args)
    if low_limit==None:
        return min(args)
    else:
        L= [x for x in args if x>=0]
        print(L)
        return min(L)

print(mini(1,2,3,4,5,6,7,-1))  """


"""l=[10,20,30,40,50]
index=int(input("Enter the Number :"))
try :
    print(l[index])
    print('Here Try statement completed Successfully')
except IndexError as msg:
    print(msg)

except ValueError as msg:
    print(msg)

print("Terminated successfully") """

"""def div(a,b):
    if b!=0:
        c=a//b
        return c

    else :

        raise ZeroDivisionError


try:
    print(div(10,0))
except:
    print("Zero Division error") """



"""print("Before Try")

try:
    a=int(input("Enter the Number"))
    b=int(input("Enter the Number"))
    c=a//b
    print("Try Block Executed")
10
except ZeroDivisionError as z:
    print(z)

else:
    print("Division is ",c)

print("Outside Try-Except Block ")"""




"""x=["10.10.10.1","10.10.10.2"]
 for i in x:
    print(i)"""

"""new=open("mydata.txt","r")
str1=new.read(7)
print(str1)
print(type(str1))
new.close() """


"""file=open("Modedemo.txt", "r+")
new=file.read(10)
print(new)
file.write("Good Bye \n")

#file.write("It will test the append things \n")
file.close() """

"""f=open("Mydata.txt","rt")
content=f.read()
print(content)
f.close() """


"""f=open("/Users/rdwived2/PycharmProjects/pythonProject/Mydata.txt") """




"""with open("Mydata.txt") as file:
    content=file.read()
    print(content)

print(file.closed)
    file.read() """


########### READING FILES INTO LIST #############



# 1.f.read.splitlines()
""""with open("Mydata.txt") as f:
    content=f.read().splitlines()
    print(content)

print("#"* 50)

with open("Mydata.txt") as f:
    content=f.readlines()
    print(content)

with open("Mydata.txt") as f:
    print(f.readline(),end="")
    print(f.readline())



print("#"*50 )


with open("Mydata.txt") as f:
    content=list(f)
    print(content) """

"""with open("Mydata.txt") as f:
    for line in f:
        print(line,end="") """

"""with open("Mydata.txt") as f:
    print(f)


# Writing to Text files

with open("Newfile.txt","w") as f:
    f.write("Just a line\n")
 #   f.close()
    f.write("This is a new line")

with open("Newfile.txt","a") as f:
    f.write("This is a new line \n this is a new line")
    print()


with open("Newfile.txt", "r+") as f:
    f.seek(5)
    f.write("100")
    f.write("Lines added with r+")
    f.seek(10)
    print(f.read()) """




"""with open("devices.txt") as d:
    content= d.read().splitlines()
    print(content)
    devices=list()
    for line in content[1:]:
        devices.append(line.split(":"))
    print(devices)

    for device in devices:
        print(f"pinging {device[1]}") """




"""with open("devices.txt") as d:
    content=d.read().splitlines()
    print(content)

    l=[]
    for i in content:
        l.append(i.split(":"))

    print(l) """

"""import csv
with open("airtravel.csv", "r") as f:
    reader=csv.reader(f)
    l=[]
    for i in reader:
        l.append(str(i))
    print(l)

    print(l)
    next(reader)
    print(reader)
    d=dict()
    for row in reader:
        print(row)
        d[row[0]]= row[1]

    print(d) """


"""with open("Macfile.txt") as f:
    content=f.read().splitlines()
    print(content)
    l=[]
    for mac in content:
        if mac in l:
            pass
        else:
            l.append(mac)
    print(l) """

"""with open("Newfile.txt") as f:
    content=f.read().splitlines()
    print(content)
    mystr="/n".join(content)
    print(mystr) """


def tail(file_name,num):
    with open(file_name,"r") as f:
        content=f.read().splitlines()
#        print(content)

    last=content[len(content)-num:]
#    print(last)
    my_str="\n".join(last)
    return my_str


while True:
    x = tail("Newfile.txt",10)
    print(x)
    time.sleep(3)
    print("")
