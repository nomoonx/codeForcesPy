__author__ = 'noMoon'

import math

[n,m,a]=map(int,raw_input().split())
print int(math.ceil(float(m)/a))*int(math.ceil(float(n)/a))