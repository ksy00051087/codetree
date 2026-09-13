N = int(input())

for _ in range(N):
    arr = input().split()
    a = int(arr[0])
    sum_val = 0
    while a != 1:
        if a % 2 == 0:
            a //= 2
            sum_val += 1
        else:
            a = a * 3 + 1
            sum_val += 1
    print(sum_val)
        
    
