def heads(numhead, numleg):
    print('Number of rabbits',(numleg-2*numhead)//2 )
    print('Number of chickens',(numhead-(numleg-2*numhead)//2))

numhead, numleg= map(int, input().split())
heads(numhead, numleg)
