a,b = map(int,input().split())
l=list(map(int,input().split()))
l1=0
r=0
add=0
found=False
while r<a:
    add+=l[r]
    while add>b:
        add-=l[l1]
        l1+=1
    if add==b:
        found=True
        print(l1,r)
        break
    r+=1
if not found:
    print(-1 , -1)