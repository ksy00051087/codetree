# a = int(input())

# for i in range(a):
#     for j in range(2 * i):
#         print(" ", end = "")
#     for j in range((2 * a) - (2 * i) - 1):
#         print('*', end = ' ')
#     print()

# for i in range(a - 1):
#     for j in range(a - (i*2)):
#         print(" ", end = '')
#     for j in range(3 + (2 * i)):
#         print('*', end = ' ')
#     print()

N = int(input())



for i in range(N, 1, - 1):
    for j in range(N - i):
        print("  ", end = "")

    for j in range(2 * i - 1):
        print('*', end = ' ')
    print()

for i in range(N):
    for j in range(N-i-1):
        print("  ", end = "")
    for j in range(2 * i + 1):
        print('*', end = ' ')
    print()