nums = list(map(int, input().split()))
up_5 = []
down_5 = []
for i in nums:
    if 500 > i:
        down_5.append(i)
    else:
        up_5.append(i)
print(f'{max(down_5)} {min(up_5)}')