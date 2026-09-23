N = 5

arr = [list(map(ord, input().split()))
for _ in range(N)]

for i in range(N):
    for j in range(3):
        a = (arr[i][j] - 32)
        print(chr(a), end = ' ')
    print()



# # print(ord(x))        
# print(chr(x))    
# # chr(ord(x) + 1) 
