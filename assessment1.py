import re

def isValidDomain_in_wordpress(str):
    regex = "^((?!-)[A-Za-z0-9-]" + "{1,63}(?<!-)\\.)" + "+[A-Za-z]{2,6}"

    p = re.compile(regex)

    if (str == None):
        return False

    if (re.search(p, str)):
        return True
    else:
        return False

str1 = "whitehouse.gov"
print(isValidDomain_in_wordpress(str1))
