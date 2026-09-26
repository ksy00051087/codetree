# Given input:
n = int(input())
answer = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for row in range(n):
    answer[row][0] = 1

# When
for row in range(1, n):
    for col in range(1, row + 1):
        answer[row][col] = answer[row - 1][col - 1] + answer[row - 1][col]

# Then output:
for row in answer:
    for elem in row:
        if elem != 0:
            print(elem, end=" ")
    print()
