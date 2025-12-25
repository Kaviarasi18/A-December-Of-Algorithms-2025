st = list(map(int, input().split(",")))
max_r = 0
can_r = True
for i in range(len(st)):
    if i > max_r:
        can_r = False
        break
    max_r = max(max_r, i + st[i])
if can_r:
    print("true")
else:
    print("false")
