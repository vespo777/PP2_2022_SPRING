n = int(input())
d={}
d1={}
for x in range(n):
    a,b = input().split()

    if b in d.keys():
        d[b] += 1
    else:
        d[b] = 1
    d1[b] = 0


m= int(input())
for x in range(m):
    a,b,c = input().split()
    
    if b in d1.keys():
        d1[b] += int(c)
    else:
        d1[b] = int(c)
sum=0
for x, v in d.items():
    if d1[x]-d[x]<0:
        sum += abs(d1[x]-d[x]) 
print ("Demons left: "+str(sum))


