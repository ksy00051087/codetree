a, b = map(int, input().split())
i = a // b
r = a % b

print(i, end='.')
for _ in range(20):
    r *= 10
    print(r // b, end='')
    r %= b
print()