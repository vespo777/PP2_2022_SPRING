import re

txt = "Amsterdam abba aba"
x = re.search("ab*", txt)
print(x)