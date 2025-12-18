n = int(input())
l=list(map(int,input().split()))
sum=0
for x in l:
    if l.count(x)==1:
        sum+=x
print(sum)