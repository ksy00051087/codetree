N = int(input())
price = list(map(int, input().split()))

min_price = price[0]
max_p = 0
for i in price[1:]:
    p = i - min_price
    if p > max_p:
        max_p = p
    if i < min_price:
        min_price = i

print(max_p)
