n=int(input())
x=n*n
z=0
while x>0:
    l=x%10
    z+=l
    x=x//10
if n==z:
    print("Neon Number")
else:
    print("Not Neon Number")