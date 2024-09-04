import math

height,weight=map(int,input().split())
if bmi >= 25:
    c = True
bmi=(10000*weight)/(height**2)
bmi= int(math.floor(bmi*10)/10)
print(bmi)
if C:
    print("Obesity")