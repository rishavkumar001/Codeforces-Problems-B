n=int(input())
l=list(map(int,input().split()))
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
c=0
for i in range(1,n+1):
    if i not in d:
        c+=1
print(c)