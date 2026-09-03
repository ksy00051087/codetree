a = int(input())
b = [int(input()) for _ in range(a)]

for i in b:
    if i % 3 == 0 and i % 2 == 1:
        print(i)