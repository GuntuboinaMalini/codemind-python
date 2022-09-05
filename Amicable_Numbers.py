n=int(input())
m=int(input())
s=0
for i in range(1,n):
    if n%i==0:
        s+=i
c=0
for j in range(1,m):
    if m%j==0:
        c+=j
if (s==m and c==n):
    print("Amicable")
else:
    print("Not Amicable")