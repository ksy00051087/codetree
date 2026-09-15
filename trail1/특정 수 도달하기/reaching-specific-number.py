arr = list(map(int, input().split()))
sum_val = 0
arr1 = []
for i in arr:
    if i > 250:
        break
    sum_val += i
    arr1.append(i)
avr = sum_val / len(arr1)

print(f'{sum_val} {avr:.1f}')
        
