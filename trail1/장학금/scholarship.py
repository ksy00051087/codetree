a, b = map(int, input().split())
a1 = (a >= 90)
if a1 and b >= 95:
    print(100000)
elif a1 and b >= 90:
    print(50000)
else:
    print(0)