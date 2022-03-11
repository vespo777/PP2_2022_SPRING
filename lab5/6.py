import re

txt = "Amsterdam dfgabba ,a.b.ab"
x = re.sub("[ .,]", ":", txt)

print(x)