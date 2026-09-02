ma1, en1 = map(int,input().split())
ma2, en2 = map(int,input().split())

if ma1 > ma2:
    print("A")
elif ma2 > ma1:
    print("B")
elif ma1 == ma2 and en1 > en2:
    print("A")
else:
    print("B")