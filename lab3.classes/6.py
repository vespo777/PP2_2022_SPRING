import math
l = [int(x) for x in input().split()]
new_l=[]
for x in l:
    b = True
    for y in range(2, int(x**0.5)):
        if x %y==0:
            b = False
    if x == 4:
        b= False
    if b:
        new_l.append(x)
print(new_l)