n1=int(input())
l1=list(map(int,input().split()))
n2=int(input())
l2=list(map(int,input().split()))
s1=0
s2=0
d={}
for i in range(len(l1)):
    d[l1[i]]=i
for i in range(len(l2)):
    if l2[i] in d:
        s1+=d[l2[i]]+1
        s2+=n1-d[l2[i]]
print(s1,end=" ")
print(s2)