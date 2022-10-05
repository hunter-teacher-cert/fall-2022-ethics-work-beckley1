# Willy Wonka search by Ben Eckley
# With a TON of help from Kiana Herr

import re


def find_name(line):
    pattern = r"((?:[A-Z][a-z,]*\.?\-? ?)+)"
    result = re.findall(pattern,line)
    
    return result


f = open("names.txt")
for line in f.readlines():
    #print(line)
    result = find_name(line)
    if (len(result)>0):
        print(result)
