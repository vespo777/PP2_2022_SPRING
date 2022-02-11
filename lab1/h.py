s = str(input())
c = str(input())
min=1111111
max=-1111111

cnt=0
i=0

for x in s:
if x==c:
cnt+=1
if i<min:
min=i
if i>max:
max=i
i+=1

if cnt == 1:
print(min)
elif cnt >1:
print (min,end=" ")
print (max, end=" ")