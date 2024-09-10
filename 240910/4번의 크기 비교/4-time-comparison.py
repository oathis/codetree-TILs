a =int(input())
b,c,d,e=map(int,input().split())
blank=[b,c,d,e]
for _ in blank:
    print(1) if a>_ else print(0)