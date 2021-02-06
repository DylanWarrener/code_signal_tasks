import math

def centuryFromYear(year):
    if 1 <= year <= 2005:
        return int(math.ceil(year / 100.0))
    else:
        return 

print(centuryFromYear(2000))
print(centuryFromYear(2006))