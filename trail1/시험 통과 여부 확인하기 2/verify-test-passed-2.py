N = int(input())
cnt = 0
for _ in range(N):
    sum_val = 0
    arr = list(map(int, input().split()))
    for i in arr:
        sum_val += i
    if sum_val // 4 >= 60:
        cnt += 1
        print("pass")
    else:
        print('fail')
print(cnt)
    
        