n=int(input())
for row in range(-n,n+1):
    top=n-abs(row)
    for i in range(abs(row)):
        print("",end="")
    for i in range(top):
        print(i,end=" ")
    for i in range(top,0,-1):
        print(i,end=" ")
    print(0)