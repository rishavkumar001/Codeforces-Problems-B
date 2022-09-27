n,a=map(int,input().split())
l=[]
l=list(map(int,input().split()))
l.sort()
s=0
for i in range(1,len(l)):
    s=max(s,abs(l[i]-l[i-1]))
s=max(s,l[0]*2,(a-l[-1])*2)
t=0.0000000000
x=s/2+t
print(x)