
N = int(input())
count_arr = [0] * 10
arr = list(map(int, input().split()))
for i in arr:
    count_arr[i] += 1
for j in count_arr[1::]:
    print(j)