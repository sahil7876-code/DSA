#Find the smallest and Largest Element: Write a program to accept N integers into an array and 
# find and display the largest element, second largest element, smallest element, second smallest element present 
# in the array. 

n = int(input("Enter numbers for array: "))
a = []

for i in range(n):
    num = int(input("Enter numbers: "))
    a.append(num)
print(a)

largest = a[0]
sec_large = a[0]
smallest = a[0]
sec_small = a[0]

for i in a:
    if i < smallest:
        sec_small = smallest
        smallest = i
    elif i < sec_small:
        sec_small = i

    if i > largest:
        sec_large = largest
        largest = i
    elif i > sec_large:
        sec_large = i

print("Smallest element:", smallest)
print("Second smallest element:", sec_small)
print("Largest element:", largest)
print("Second largest element:", sec_large)