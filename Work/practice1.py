def sumcount(n):
    '''
    Returns the sume of the first n integers
    '''
    total = 0
    while n > 0:
        total += 1
        n -= 1
    return total

import math
x = math.sqrt(10)

import urllib.request
u = urllib.request.urlopen('http://www.python.org/')
data = u.read()


''' this is an example showing try and except case

for line in f:
    fields = line.split()
    try:
        shares = int(fields[1])
    except ValueError:
        print("Couldnt parse", line)
'''