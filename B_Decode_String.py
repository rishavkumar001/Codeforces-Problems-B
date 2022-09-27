for _ in range(int(input())):
    n=int(input())
    k=int(input())
    s=""
    while k!=0:
        if k%10==0:
            k=k//10
            p=k%100
            s=s+chr(96+p)
            k=k//100
        else:
            p=k%10
            s=s+chr(96+p)
            k=k//10
    print(s[::-1])