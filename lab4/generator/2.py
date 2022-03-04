n = int(input())
a = (i for i in range(n) if i%2==0)
for i in a:
    if n-i==1 or n-i==2:
        print(i)
    else:
        print(i,end=", ")