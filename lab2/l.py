s=str(input())
a=[]


for i in range(len(s)):
    if s[i]=='(' or s[i]=='{' or s[i]=='[':
        a.append(s[i])

    elif s[i]==')':
        if len(a)==0:
            print("No")
            exit()
        elif a[-1]=='(':
            a.pop()
        else:
            print("No")
            exit()

    elif s[i]=='}':
        if len(a)==0:
            print("No")
            exit()
        elif a[-1]=='{':
            a.pop()
        else:
            print("No")
            exit()

    elif s[i]==']':
        if len(a)==0:
            print("No")
            exit()
        elif a[-1]=='[':
            a.pop()
        else:
            print("No")
            exit()



if len(a)==0:
    print("Yes")
else:
    print("No")

        