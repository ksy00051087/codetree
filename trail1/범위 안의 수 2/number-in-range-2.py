
arr = [int(input()) for _ in range(10)]
sum_val = 0
total = 0

for i in arr:
    if 0 <= i <= 200:
        sum_val += i
        total += 1
sum_av = ((sum_val) / (total))
print(f'{sum_val} {sum_av:.1f}')