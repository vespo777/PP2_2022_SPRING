n = int(input())
a = (i for i in range(n) if i%3==0 or i%4==0)
for i in a:
    print(i)