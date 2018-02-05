# Come up with a regular expression that 
# matches all the digits in the string
# Arizona 479, 501, 870. Califonia 209,
# 213, 650.

import re

line = "Arizona 479, 501, 870. Califonia 209, 213, 650."

match = re.findall("\d", line, re.IGNORECASE)

print(match)
