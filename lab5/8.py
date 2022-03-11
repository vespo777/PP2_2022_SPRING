import re

txt = "The rain in Spain"
x = re.split("[A-Z]", txt)
print(x)