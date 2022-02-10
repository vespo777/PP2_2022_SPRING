n,x = map(int,input().split())

l = []

for y in range(n):
    a=x+2*y
    l.append(a)
for y in range(1,n):
    sum = l[y-1] ^ l[y] 




print(l)
print(sum)