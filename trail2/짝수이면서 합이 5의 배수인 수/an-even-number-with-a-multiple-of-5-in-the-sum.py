n = int(input())

def syg(n):
    a = (n // 10) + (n % 10)
    if n % 2 == 0 and a  % 5 == 0:
        print('Yes')
    else:
        print('No')
    return
    

syg(n)