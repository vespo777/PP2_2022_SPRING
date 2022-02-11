a, b= input(). split()
a = int(a)
b = int(b)

ans = True
i = 2
while i <= a ** 0.5:
if a%i ==0:
ans=False
i+=1

if a<=500 and ans and b%2==0 :
print ("Good job!")
else :
print ("Try next time!")