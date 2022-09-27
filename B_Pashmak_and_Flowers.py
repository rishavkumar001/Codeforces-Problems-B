n=int(input())
l=list(map(int,input().split()))
l.sort()
a=l[0]
b=l[-1]
ca,cb=0,0
if a==b:
    print(b-a,end=" ")
    print(n*(n-1)//2)
else:
    for i in l:
        if i==a:
            ca+=1
        if i==b:
            cb+=1
    print(b-a,end=" ")
    print(ca*cb)