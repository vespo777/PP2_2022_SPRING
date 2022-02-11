n = int(input())

i=n-1
j=0
for x in range(n):
    for y in range(n):
        if n%2==1:
            if y>=i:
                print ("#", end="")
            else:
                print (".", end="")
        else :
            if y>j:
                print (".",end="")
            else:
                print ("#",end="")
    i-=1
    j+=1
    print("")