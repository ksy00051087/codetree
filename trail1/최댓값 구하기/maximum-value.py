a, b, c = map(int, input().split())

if a <= b and b <= c and a <= c:
    print(c)
elif a <= b and b >= c and a <= c:
    print(b)
elif a >= b and b <= c and a <= c:
    print(c)
elif a <= b and b >= c and a >= c:
    print(b)
elif a >= b and b <= c and a >= c:
    print(a)
elif a >= b and b >= c and a >= c:
    print(a)
else:
    print()