import re

target_string = "Vishli! dot.com; is for, Python-program?"
result = re.split(r"[\b\W\b]+", target_string)
print(result)

