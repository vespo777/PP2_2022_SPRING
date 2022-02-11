x1,y1=map(int, input().split())
n=int(input())
points=[]


for i in range(n):
    cord=input()
    x2,y2=map(int, cord.split())

    distance=(x2-x1)**2+(y2-y1)**2

    points.append((cord,distance))

points.sort(key=lambda x:x[1])

for i in points:
    print(i[0])
