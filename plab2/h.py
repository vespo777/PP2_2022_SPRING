a,b = map(int, input().split())

n = int(input())
d={}
for x in range(n):
    a,b = map(int, input().split())
    d[a]=b
min=111111111111


for x in range(n):
    for y, v in d.items():
        if (a-y)**2+(b-v)**2<min:
            min = (a-y)**2+(b-v)**2
            k=y
            l=v
        print((a-y)**2+(b-v)**2)

    print(k, l)

    d[k]=111111111111
    min=11111111111111

