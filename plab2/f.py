import collections
n =int(input())
d={}

for x in range(n):
    a,b= input().split()
    
    if a in d.keys():
        d[a] += int(b)
    else:
        d[a] = int(b)
od = collections.OrderedDict(sorted(d.items()))

max =0
for k, v in od.items():
    
    
    if v > max:
        max = v
        

for k, v in od.items():
    if v == max:
        print(str(k)+" is lucky!")
    else:
        print(str(k)+ " has to receive "+str(max-v)+" tenge")
