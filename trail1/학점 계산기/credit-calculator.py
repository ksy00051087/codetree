N = int(input())
arr = list(map(float, input().split()))
sum_val = sum(arr[0:])

avr = sum_val / N
print(f'{avr:.1f}')
if avr >= 4.0:
    print("Perfect")
elif avr >= 3.0:
    print("Good")
else:
    print('Poor')

