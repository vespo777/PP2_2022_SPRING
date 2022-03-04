import json

a = json.load(open(r"C:\Users\tileu\Desktop\istok\lab4\data.txt"))

print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")

for i in a["imdata"]:
    print(i["l1PhysIf"]["attributes"]["dn"]," "*28,i["l1PhysIf"]["attributes"]["fecMode"]," "*1,i["l1PhysIf"]["attributes"]["mtu"])