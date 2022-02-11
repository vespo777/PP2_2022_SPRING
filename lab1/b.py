s = str(input())
i=0
for x in s:
    i+=ord(x)

if i>300:
    print("It is tasty!")
else:
    print("Oh, no!")