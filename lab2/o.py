def atoint(a):
    res=""
    s=""
    for x in a:
        s=s+x
        

        if len(s)==3:
            res += d[s]
            s=""
    return res

d = {}
d["ONE"]="1" 
d["TWO"]="2"
d["THR"]="3" 
d["FOU"]="4" 
d["FIV"]="5"
d["SIX"]="6" 
d["SEV"]="7" 
d["EIG"]="8"
d["NIN"]="9" 
d["ZER"]="0"  
a = str(input())
f=""
s=""
cnt=0
for x in a:
    if x=="+":
        cnt=1

    if cnt==0:
        f=f+x
    elif cnt==1 and x !="+":
        s=s+x
sum= int(atoint(f))+int(atoint(s))

for x in str(sum):
    if x== "0":
        print("ZER",end="")
    if x== "1":
        print("ONE",end="")    
    if x== "2":
        print("TWO",end="")
    if x== "3":
        print("THR",end="")
    if x== "4":
        print("FOU",end="")
    if x== "5":
        print("FIV",end="")
    if x== "6":
        print("SIX",end="")
    if x== "7":
        print("SEV",end="")
    if x== "8":
        print("EIG",end="")
    if x== "9":
        print("NIN",end="")
    
    










