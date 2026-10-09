'''
#sum of numbers 1 to 10

sum=0
for i in range(1,11):
    sum = sum+i
print("Sum of numbers 1 to 10 is: ",sum)


#Printing Multiplication table of a given number

n=18
for i in range(1,11):
    print(n,"*",i,"=",n*i)

    
#Print numbers from 1-10 using  loop

for i in range(1,11):
    print(i)


#Find greateast of 2 numbers

n1=int(input("Enter a number: "))
n2=int(input("Enter a number: "))

if n1 > n2:
    print(n1,"is greater")
else:
    print(n2, "is greater")


#check odd or even

num=int(input("ENter a num: "))

if num%2==0:
    print("Number is even")
else:
    print("NUmber is odd")

    
#eligible to vote

age=int(input("Enter age: "))

if age > 18:
    print("Eligible to vote")
else:
    print("Not Eligible")

    
#check pos or neg
num=int(input("Enter number"))

if num > 0:
    print("Num is pos")
elif num==0:
    print("num is 0")
else:
    print("Num is neg")    

    
#calculate SI

p=int(input("ENter p"))
r=int(input("ENter r"))
t=int(input("ENter t"))

SI=(p*r*t)/100
print(SI)


#area of rect

l=int(input("Enter l"))
b=int(input("Enter b"))

print(l*b)


#disp sum

l=int(input("Enter l"))
b=int(input("Enter b"))

print(l+b)


#display name, class, s name

n=input("Enter Name: ")
c=int(input("Enter Class: "))
s=input("Enter School Name: ")

print("Name:",n,"\n Class",c,"\n School Name:", s)


'''