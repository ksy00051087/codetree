a = int(input())

for i in range(a):
    for j in range(a - i):
        print('*', end = '')    
    for j in range(2 * i - i):
        print("  ", end = "")    
    for j in range(a - i):
        print('*', end = '')
    print()

