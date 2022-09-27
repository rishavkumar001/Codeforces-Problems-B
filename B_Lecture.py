n,m=map(int,input().split())
d={}
for i in range(m):
    a,b=input().split()
    if len(a)>len(b):
        b=b+'1'
    else:
        b=b+'0'
    d[a]=b
l=list(input().split())
for i in l:
    if d[i][-1]=='0':
        print(i,end=" ")
    else:
        print(d[i][:-1],end=" ")