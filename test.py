
"""def fact(num):
    result =1
    for i in range(num):
        result=num*result
        num = num-1
    return result

x= fact(5)
print(x) """
from itertools import count
from os import WCONTINUED
from pickle import STRING

"""x=[]
y=tuple()
print(id(x))
for i in range(5):
    a=int(input("Enter the Number"))
    x.append(a)
    y.insert(a)

print(x)
print(id(x))"""

""""
a= input("Enter the world")
print(a.upper()) """


"""x=[]
for i in range(5):
    a=input("Enter the Number :")
    if len(a)==4 and int(a) % 5 ==0:
        x.insert(i, a)
    else:
        continue
print(x) """




"""a= input("Enter the alphanumeric :")
count1,count2=0,0
for i in a:
  #  print(i)
    if i.isdigit():
        count1=count1+1
       # print(count1)

    elif i.isalpha():
        count2=count2+1
      #  print(count2)
    else:
        continue

print(count1,count2)"""



### Program for Variable Length Argument in Python

"""a = 10
def som():
    global a
   #  a = 30
    print("In fun",a)
    a=30


# print("Outside",a)
som()
print("outside",a ) """

"""a = 10
def som():
    x = globals()["a"]
    globals()["a"]=100
    a = 30
    print("In fun",a


# print("Outside",a)
som()
print("outside",a) """

"""def count(list):
    even=0
    odd=0
    for i in list:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd



list=[20,25,15,14,19,24,27]

x,y = count(list)

print("Even : {} and Odd:{}".format(x,y)) """




"""a="Hellomy,nameis,rohit"
y=a.split(",")
print(y) """

################################## Banking Program #####################################
""""sum =0
while True:

    a=int(input("Press 1 for Deposit and Press 2 for Withdrawl"))
    if a== 1:
        d = int(input("Enter the amount you want to deposit"))
        sum= sum+d
        print("Thanks for choosing us")
    elif a==2:
        w= int(input("Enter the amount you want to withdrawl"))
        sum= sum-w
        print("Thanks for choosing us")
    else:
        pass

    print("Total balance in your account is ", sum) """


    ##########################Program for Password check ###########################

"""import re
x=[]
user_name= input("Enter the username : ")
while True:
    password = input("Enter the Password : ")
    x.append(password)
    for i in x:
        if len(i) < 6 or len(i) > 12:
            continue
        elif re.search("[a-z]",i)  and re.search("[0-9]",i) and re.search("[A-Z]",i) and re.search("[$#@]",i) :
            print(i)
        else:
            print("Sorry you haven't met the passowrd requirement, Please retry to set the password")
        break
#    print()
#print() """

################################### Fibonacci Series in python ########################
"""a=0
b=1

for i in range(0,6):
    c=a+b
    a=b
    print("Current value of a is",a)
    b=c
    print("Current value of b is",b)
    print(c) """


################################## Program to calculate the squre of Number #########

"""def squ(num):
    for i in range(num,0,-1):
        num=num*num
        break
    return num
x= squ(5)
print(x) """


##############################

"""x=(1,2,3,4,5,6,7,9)
count=0
for i in x:
    count+=1 """

################################# Recursion in Python ##############################

"""def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)

result = fact(5)
print(result) """




