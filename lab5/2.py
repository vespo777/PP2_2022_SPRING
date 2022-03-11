import re

txt = "Amsterdam ahgb abbb aba"
x = re.findall("a.{2,3}b", txt)
print(x)