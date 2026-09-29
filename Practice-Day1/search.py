#Write a program to accept N integers into an array and search for a given number. 
#Display an appropriate message indicating whether the number is present in the array or not and 
# also display its position. 

n = int(input("Enter numbers for array: "))
a = []

for i in range(n):
    num = int(input("Enter numbers: "))
    a.append(num)
print(a)


search = int(input("Enter a number to search: "))
if search in a:
    print("Element found at position: ",a.index(search))
else:
    print("Element not in the list")