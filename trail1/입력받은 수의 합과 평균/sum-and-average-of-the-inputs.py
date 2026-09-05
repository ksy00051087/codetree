N = int(input())
arr = [int(input()) for _ in range(N)]
sum = 0
total = 0
for i in arr:
    sum += i
    total += 1
avr = ((sum) / (total))
print(f'{sum} {avr:.1f}')

