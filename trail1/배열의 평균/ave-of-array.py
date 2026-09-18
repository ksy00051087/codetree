arr = [list(map(int, input().split())) for _ in range(2)]
arr1 = []
for j in range(2):
    b = sum(arr[j]) / 4
    arr1.append(b)
    print(f'{b:.1f}', end = ' ')
print()
for i in range(4):
    a = (arr[0][i] + arr[1][i]) / 2
    arr1.append(a)
    print(f'{a:.1f}',end = ' ')
print()
print(f'{sum(arr1) / len(arr1):.1f}')
