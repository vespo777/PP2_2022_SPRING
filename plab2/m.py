import collections
l=[]
b=0
while b!=1 :
    a = str(input())
    if a=="0":
        break
    else:
        l.append(a)
d={}
sum=0
l1=[]
m=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for x in l:
    l1=[int(a) for a in x.split()]
    sum = l1[0] + m[l1[1]-1]+ 365*l1[2]
    d[sum]=x

od = collections.OrderedDict(sorted(d.items()))
for k, v in od.items(): print(v)