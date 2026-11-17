a, b = map(int, input().split())

def is_target(n):
    if n % 3 == 0:
        return True
    for ch in str(n):
        if ch in '369':
            return True
    return False


def count_targets(a, b):
    cnt = 0
    for i in range(a, b + 1):
        if is_target(i):
            cnt += 1
    return cnt

print(count_targets(a, b))