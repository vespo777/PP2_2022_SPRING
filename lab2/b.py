a = int(input())
l =[]
l = [ int(x) for x in input().split()]
l.sort()
i=len(l)


print(l[i-2]*l[i-1])