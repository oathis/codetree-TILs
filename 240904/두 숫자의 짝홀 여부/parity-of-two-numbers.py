a, b = map(int,input().split())
list=[a,b]
for i in list:
    if i %2 == 0:
        print("even")
    else:
        print("odd")