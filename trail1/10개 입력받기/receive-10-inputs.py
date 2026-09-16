arr = list(map(int, input().split()))
arr1 = []
sum_val = 0
for i in arr:
    if i == 0:
        break
    arr1.append(i)
sum_val = sum(arr1)
avr = sum_val / len(arr1)
print(f'{sum_val} {avr:.1f}')