arr =[]
final_arr = []
for index in range(int(input())):
    book = input().split()
    if book[0]=="1":
        arr.append(book[1])
    else:
        if len(arr)==0:
            pass
        else:
            final_arr.append(arr.pop(0))
print(*final_arr)