import os
print('Exist:', os.access(r"C:\Users\ast\Desktop\ag c++\lab6", os.F_OK) )
print('Readable:', os.access(r"C:\Users\ast\Desktop\ag c++\lab6", os.R_OK))
print('Writable:', os.access(r"C:\Users\ast\Desktop\ag c++\lab6", os.W_OK))
print('Executable:', os.access(r"C:\Users\ast\Desktop\ag c++\lab6", os.X_OK))