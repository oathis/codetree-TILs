import math

a = int(input())
if a%2 == 0:
    print(int(a/2))
else:
    print(math.floor((a+1)/2))