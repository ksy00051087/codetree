N = int(input())
mul_val = 1
for _ in range(N):
    arr = input().split()
    a, b = int(arr[0]), int(arr[1])

    for i in range(a, b + 1):
        mul_val *= i
    print(mul_val, end = ' ')
    mul_val = 1
    print()