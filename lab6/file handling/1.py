import os


def fileees(path):
    for i in os.listdir(path):
        print(i)

path = r"C:\Users\ast\Desktop\ag c++\lab6"
fileees(path)