#Calculate Array Sum: Write a program to accept N integers into an array and calculate and 
# display the sum of all the elements. 

n=int(input("Enter numbers for array: "))
sum=0
a=[]

for i in range(n):
    num=int(input("Enter numbers: "))
    a.append(num)

for j in a:
    sum+=j
print(sum)