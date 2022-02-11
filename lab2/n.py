l=[]
for x in range(10**5):
    a= int(input())
    if a!=0:
        l.append(a)
    else:
        break

k=len(l)
if k%2==0:
    for x in range(int(k/2)):
        print(l[x]+l[k-1-x], end=" ")
else:
    for x in range(int(k/2)+1):
        if x == int(k/2):
            print(l[x], end=" ")
        else:
            print(l[x]+l[k-1-x], end=" ")

    
