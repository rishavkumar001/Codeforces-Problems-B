n=int(input())
l=list(map(int,input().split()))
d={}
for i in range(1,5):
    d[i]=0
for i in l:
    d[i]+=1
c=0
c+=d[4]
c+=d[3]
if d[1]>d[3]:
    d[1]-=d[3]
else:
    d[1]=0
c+=d[2]//2
if d[2]%2!=0:
    c+=1
    if d[1]>1:
        d[1]-=2
    else:
        d[1]=0
c+=d[1]//4
if d[1]%4!=0:
    c+=1
print(c)