n = int(input())

c1=0
c2=0
c3=0
l=[]
s=set()
for x in range(n):
    a = input()
    for y in a:
        if ord(y)>=48 and ord(y)<=57:
            c1= 1
        elif ord(y)>=65 and ord(y)<=90:
            c2=1
        elif ord(y)>=97 and ord(y)<=122:
            c3=1
    if c1==1 and c2 ==1 and c3 ==1:
        l.append(a)
    c1=0
    c2=0
    c3=0
cnt=0
for x in l:
    for y in l:
        if x==y:
            cnt+=1
            if cnt==2:
                l.remove(y)
                cnt-=1
    cnt=0    
        

l.sort()
print(len(l))
for x in l:
    print(x)

