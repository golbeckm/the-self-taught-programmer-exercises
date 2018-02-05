# Create a regular expression that matches
# any word that starts with any character 
# and is followed by two o's. Then use Python's
# re module to match boo and loo in the sentence
# The ghost that says boo haunts the loo.

import re

line = "The ghost that says boo haunts the loo."

match = re.findall(".oo", line, re.IGNORECASE)

print(match)
