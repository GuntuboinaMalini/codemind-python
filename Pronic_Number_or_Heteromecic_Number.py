n=int(input())
t=0
for i in range(n):
    if i*(i+1)==n:
        t=1
        break
if t==1:
    print("YES")
else:
    print("NO")