for _ in range(int(input())):
    n=int(input())
    if n==1:
        print(0)
    else:
        a,b=0,0
        while n%2==0:
            a+=1
            n=n//2
        while n%3==0:
            b+=1
            n=n//3
        if n==1 and a<=b:
            print(2*b-a)
        else:
            print(-1)