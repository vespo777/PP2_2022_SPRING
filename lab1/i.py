a = int(input())

while a>0:
b=str(input())
x= b.find("@gmail.com")
if x != -1:
ans = b.replace("@gmail.com", "")
print (ans)
a-=1