N,X=map(int,input().split())
s=str(N)
l=len(s)
a=int(s[l-X:l])
b=int(str(N)[:X])
if a>b:
    print(a-b)
else:
    print(b-a)

