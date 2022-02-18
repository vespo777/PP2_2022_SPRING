from itertools import permutations 
def permute(s):
    perm= permutations(s)
    for i in list(perm):
        print(i)


l= [ x for x in input()]
permute(l)


