num=int(input("Enter a number to reverse it: "))
sum=0
n=num

while(n>0):
    sum=sum*10+(n%10)
    n//=10

if(num==sum):
    print(num,"is a palindrome number")
else:
    print("Not plindrome")