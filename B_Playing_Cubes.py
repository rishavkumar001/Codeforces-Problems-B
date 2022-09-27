n,m=map(int,input().split())
if m<n:
    m,n=n,m
mm=m
nn=n
if m-n==1:
    print(n,end=" ")
    print(m)
else:
    l=[1]*(m+n)
    l[0]=0
    n=n-1
    for i in range(1,len(l)):
        if m==0 or n==0:
            break
        if l[i-1]==0:
            if i%2:
                m-=1
            else:
                n-=1
                l[i]=0
                
        else:
            if i%2:
                n-=1
                l[i]=0
            else:
                m-=1
    c1,c2=0,0
    for i in range(1,len(l)):
        if l[i]==l[i-1]:
            c1+=1
        else:
            c2+=1
    print(l)
    l=[1]*(mm+nn)
    l[0]=0
    mm=mm-1
    for i in range(1,len(l)):
        if mm==0 or nn==0:
            break
        if l[i-1]==1:
            if i%2:
                nn-=1
            else:
                mm-=1
                l[i]=1
                
        else:
            if i%2:
                mm-=1
                l[i]=1
            else:
                nn-=1
    c11,c22=0,0
    for i in range(1,len(l)):
        if l[i]==l[i-1]:
            c11+=1
        else:
            c22+=1
    print(l)
    if max(c1,c2)>max(c11,c22):
        print(max(c1,c2),end=" ")
        print(min(c1,c2))
    else:
        print(max(c11,c22),end=" ")
        print(min(c11,c22))
    