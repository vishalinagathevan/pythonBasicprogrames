import re

target_string = "Vishli! dot.com; is for, Python-program?"
result = re.split(r"\s", target_string)


for x in result:
    if re.findall("Vi.*li$", x):
        print (x)

