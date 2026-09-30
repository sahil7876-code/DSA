a=[10,32,5,76,9,43,23,5,1]
#len(a)

large = a[0]
sec_large=a[0]
small=a[0]
sec_small=[0]


for i in a:
    if large <i :
        large = i
        sec_large=large
    elif (i < sec_large or i!=large):
        sec_large=i
print(large)
print(sec_large)

'''if small >i :
        small = i
        sec_small=small
    elif (i < sec_small and i!=small):
        sec_small=i

print(small)
print(sec_small)'''