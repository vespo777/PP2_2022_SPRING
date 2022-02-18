def is_prime(a):
    for x in range(2, int(a ** 0.5)+1):
        if a%x == 0:
            return False
    return True
    


l = [ int(x) for x in input().split()]
for x in l:
    if is_prime(int(x)):
        print(x)
