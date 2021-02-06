'''
Given a year, return the century it is in. The first century spans 
from the year 1 up to and including the year 100, the second - 
from the year 101 up to and including the year 200, etc.

For example, for year = 1905, the output should be 
centuryFromYear(year) = 20;

For year = 1700, the output should be
centuryFromYear(year) = 17.

[constraints] - 1 ≤ year ≤ 2005.
[input] - integer year.
[output] - integer.
'''
import math

def centuryFromYear(year):
    if 1 <= year <= 2005:
        return int(math.ceil(year / 100.0))
    else:
        return 

print(centuryFromYear(2000))
print(centuryFromYear(2006))