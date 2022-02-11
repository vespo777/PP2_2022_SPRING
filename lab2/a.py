x=list(map(int,input().split()))

t=len(x)-1

for i in range(len(x)-2,-1,-1):

    if i+x[i]>=t:

        t=i

if t==0:

    print(1)

else:

    print(0)
