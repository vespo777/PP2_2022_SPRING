def uniq(l):
    d={}
    new_l=[]
    for x in l:
        d[x] = 1
    for x in d.keys():
        new_l.append(x)
    print(new_l)

list = [ str(x) for x in input().split()]
uniq(list)