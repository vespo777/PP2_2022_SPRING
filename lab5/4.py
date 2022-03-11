import re

txt = "Madrid dfgabba aba"
x = re.findall("[A-Z][a-z]", txt)
print(x)