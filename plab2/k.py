l=[]
l =[ str(x) for x in input().split()]
cnt=0
for x in l:
    
    for y in x:
        if ord(y)<65 or ord(y)>90:
            if ord(y)<97 or ord(y)>122:
                l[cnt] = l[cnt].replace(y,"")
    cnt+=1
                

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

