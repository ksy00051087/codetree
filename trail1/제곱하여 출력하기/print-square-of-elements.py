N = int(input())
arr = list(map(int, input().split()))
arr1 = [i ** 2 for i in arr]
for j in arr1:
    print(j, end = ' ')

# list_ = [(i + j) for i in range(3) for j in range(3)]
