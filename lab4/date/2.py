import datetime

x = datetime.datetime.now()
a = x - datetime.timedelta(days = 1)
b = x + datetime.timedelta(days = 1)
print(a)
print(x)
print(b)