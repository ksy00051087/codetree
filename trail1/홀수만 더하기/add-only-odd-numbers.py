a = int(input())
sum_val = 0
for _ in range(a):
    b = int(input())
    if b % 2 != 0 and b % 3 == 0:
        sum_val += b
print(sum_val) 

# n = int(input())

# for _ in range(n):
#     a = int(input())
#     if a % 2 == 1 and a % 3 == 0:
#         print(a)
