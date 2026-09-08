a = int(input())

sc = False
for i in range (2, a):
    if a % i == 0:
        sc = True

if sc:
    print("C")
else:
    print("P")