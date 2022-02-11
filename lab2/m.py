l=[]
for x in range(10**5):
    g= input()
    if g!="0":
        a, b, c= g.split()
        l.append(str(c)+" "+str(b)+" "+str(a))
    else:
        break

l.sort()

for x in l:
    a, b, c= x.split()
    print (str(c)+" "+str(b)+" "+str(a))

    




