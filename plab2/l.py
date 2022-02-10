a= str(input())
cur=0
for x in a:
    if x=="(":
        for y in a:
            if y==")":
                a=a.replace(x,"")    
                a=a.replace(y,"")

print (a)            