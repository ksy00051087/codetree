N = int(input())
arr = list(map(int, input().split()))

arr1 = sorted(arr)
print(f'{arr1[-1]} {arr1[-2]}')
