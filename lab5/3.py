import re

txt = "Amsterdam dfgabba a_ba a_v"
x = re.findall("[a-z]_[a-z]", txt)
print(x)