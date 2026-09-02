a = int(input())

if a % 2 == 0:
    if a == 2:
        print(28)
    elif a == 8 or a == 10 or a == 12:
        print(31)
    else:
        print(30)
elif a % 2 == 1:
    if a == 9 or a == 11:
        print(30)
    else:
        print(31)
