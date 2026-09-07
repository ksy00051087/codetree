cnt = 0
sum_val = 0

while True:
    n = int(input())
    if 20 <= n <= 29:
        cnt += 1
        sum_val += n
    else:
        break
avr = sum_val / cnt
print(f'{avr:.2f}')

