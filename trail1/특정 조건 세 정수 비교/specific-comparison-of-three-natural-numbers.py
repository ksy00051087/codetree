a, b, c = map(int, input().split())

a1 = ()
b1 = ()

if a <= b and a <= c:
    a1 = (1)
else:
    a1 = (0)

if a == b == c:
    b1 = (1)
else:
    b1 = (0)

print(f'{a1} {b1}')