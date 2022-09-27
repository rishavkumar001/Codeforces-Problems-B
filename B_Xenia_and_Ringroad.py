n,m=map(int,input().split())
l=list(map(int,input().split()))
s=0
for i in range(m-1,0,-1):
    if l[i]>=l[i-1]:
        s+=l[i]-l[i-1]
    else:
        s+=n-(l[i-1]-l[i])
s+=l[0]-1
print(s)
