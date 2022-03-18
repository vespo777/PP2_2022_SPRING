import os
path = r"C:\Users\ast\Desktop\ag c++\lab6"

if os.path.exists(path):
    for i in os.listdir(path):
        print(i)