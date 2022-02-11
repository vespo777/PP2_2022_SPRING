n = input().split()
if len(n) == 1:
    n = int(n[0])
    x = int(input())
else:
    n, x = int(n[0]), int(n[1])


l = []
for y in range(n):
    a=x+2*y
    l.append(a)
sum=int(l[0])
for y in range(1,n):
    sum =  sum ^ l[y]



print(sum)
