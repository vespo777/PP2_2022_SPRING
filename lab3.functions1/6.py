def rev(s):
    for x in s[::-1]:
        print (x, end=" ")


l = [ x for x in input().split()]
rev(l)
