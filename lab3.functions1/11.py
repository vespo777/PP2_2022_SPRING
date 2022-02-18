def is_palind(a):
    for x in range(int(len(a)/2)):
        if a[x]!=a[len(a)-x-1]:
            return False
    return True

a = str(input())
if is_palind(a):
    print("Yes")
else:
    print("No")
