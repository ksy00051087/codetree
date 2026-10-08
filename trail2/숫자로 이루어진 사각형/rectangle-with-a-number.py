n = int(input())

def square(num):
    cnt = 1
    for i in range(num):
        for j in range(num):
            print(cnt, end=' ')
            if cnt <= 8:
                cnt += 1
            else:
                cnt = 1
        print()
    return cnt

square(n)

