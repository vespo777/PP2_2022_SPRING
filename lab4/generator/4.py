def squares(n, m):
    while n != m - 1:
        yield n**2
        n -= 1
n = int(input())
m = int(input())

g = squares(n, m)
for i in g:
    print(i)