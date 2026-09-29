#Write a program to accept N integers into an array and display the elements in reverse order 
#without changing the original array. 

n = int(input("Enter numbers for array: "))
a = []

for i in range(n):
    num = int(input("Enter numbers: "))
    a.append(num)
print(a)

for j in a[::-1]:
    print(j)
