n = int(input())

nums = [1,2,3,4,5,6,7,8,9] * 1111 + [1]

for i, val in enumerate(nums):
    print(val, end=" ")
    if (i+1) % n == 0:
        print()
    if (i+1) == n*n:
        break
    