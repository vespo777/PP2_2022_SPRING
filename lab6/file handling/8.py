import os

if os.path.exists(r"C:\Users\tileu\Desktop\istok\lab6\text.txt"):
  os.remove(r"C:\Users\tileu\Desktop\istok\lab6\text.txt")
else:
  print("The file does not exist")