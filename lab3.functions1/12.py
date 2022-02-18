def print_histo(l):
    for x in l:
        for y in range(x):
            print("*",end="")
        print("")    


l = [ int(x) for x in input().split()]
print_histo(l)
