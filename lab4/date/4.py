import datetime

a = datetime.datetime.now()

b = datetime.datetime(2023, 1, 12)

print((b-a).total_seconds())