#Count Even and Odd Numbers: Write a program to accept N integers into an array and count and 
#display the number of even and odd elements present in the array. 

n = int(input("Enter numbers for array: "))
a = []

for i in range(n):
    num = int(input("Enter numbers: "))
    a.append(num)
print(a)

even=0

for i in a:
    if i%2==0:
        even+=1
odd=n-even
print("Even numbers:", even)
print("Odd Numbers: ", odd)