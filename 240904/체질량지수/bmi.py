import math

height,weight=map(int,input().split())
bmi=(10000*weight)/(height**2)
C=0
if bmi >= 25:
    c = 1

bmi= int(math.floor(bmi*10)/10)
print(bmi)
if c == 1:
    print("Obesity")