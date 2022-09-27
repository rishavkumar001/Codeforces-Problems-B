t=int(input())
while t!=0:
    p=list(map(int,input().split()))
    n,x,y=p[0],p[1],p[2]
    if x!=0 and y!=0:
        print(-1)
    elif y==0 and x==0:
        print(-1)
    else:
        if x<y:
            x,y=y,x
        if (n-1)%x==0:
            q=1
            y=0
            for i in range(n-1):
                if x==y:
                    y=0
                    q=i+2
                y+=1
                print(q,end=" ")
            print()   
        else:
            print(-1)
    t-=1