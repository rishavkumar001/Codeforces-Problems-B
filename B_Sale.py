from re import S


a,n=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
p=0
s=0
for i in l:
    if p!=n and i<0:
        s=s-i
        p+=1
print(s)