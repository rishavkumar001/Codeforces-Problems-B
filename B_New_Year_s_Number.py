for _ in range(int(input())):
    n=int(input())
    a=n//2020
    b=n%2020
    if a>=b:
        print("YES")
    else:
        print("NO")