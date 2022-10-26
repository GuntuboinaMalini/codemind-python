n=int(input())
sum1=0
pro=1
while n>0:
    z=n%10
    sum1= sum1 + z
    pro*=z
    n=n//10

if sum1==pro:
    print("Spy Number")
else:
    print("Not Spy Number") 