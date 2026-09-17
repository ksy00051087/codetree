a, b = map(int, input().split())
c_arr = [0] * b
while a > 1:
    c_arr[a % b] += 1
    a = a // b

print(sum(i ** 2 for i in c_arr))