#Write a program to accept N integers into an array and 
#create a new array containing only the unique elements, removing all duplicate values. 

n = int(input("Enter numbers for array: "))
a = []

for i in range(n):
    num = int(input("Enter numbers: "))
    a.append(num)

b=[]
for i in a:
    if i not in b:
        b.append(i)

print(b)