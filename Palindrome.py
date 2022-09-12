N=int(input())
s=str(N)
l=len(s)
if s[0]==s[len(s)-1]:
    print(True)
else:
    print(False)