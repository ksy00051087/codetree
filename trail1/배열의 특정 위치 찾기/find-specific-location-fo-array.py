arr = list(map(int, input().split()))
arr1 = arr[1::2]
arr2 = arr[2::3]
sum_val2 = sum(arr2)
sum_val = sum(arr1)
avr =  sum_val2 / len(arr2)

print(f'{sum_val} {avr:.1f}')