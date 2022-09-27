n,x=map(int,input().split())
s=input()
l=list(s)
l1=[]
for i in range(x):
    j=1
    while j<n:
        if l[j]=='G'and l[j-1]=='B':
            l[j],l[j-1]='B','G'
            j+=1
        j+=1
for i in l:
    print(i,end="")
print()