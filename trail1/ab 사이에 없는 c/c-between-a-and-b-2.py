a, b, c = map(int, input().split())
sc = False

for i in range (a, b + 1):
    if  i % c == 0:
        sc = True
        break
if sc:
    print("NO")
else:
    print("YES")