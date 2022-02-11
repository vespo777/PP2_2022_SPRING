n = int(input())

for x in range(n):
    for y in range(n):
        if x==y:
            print (int(x*x),end=" ")
        elif x==0:
            print (y,end=" ")
        elif y==0:
            print (x,end=" ")
        else :
            print (0, end=" ")
    print("")
        