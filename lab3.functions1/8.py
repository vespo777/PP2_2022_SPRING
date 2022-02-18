def spy_game(i):
    cnt=0
    for x in range(len(i)):
        if i[x]==0:
            if cnt<2:
                cnt+=1
        if i[x]==7 and cnt==2:
            return True
    return False



l= [int(x) for x in input().split()]

print(spy_game(l))