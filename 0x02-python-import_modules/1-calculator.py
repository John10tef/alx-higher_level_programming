#!/usr/bin/python3
from calculator_1 import add
from calculator_1 import sub
from calculator_1 import mul
from calculator_1 import div

a = 10 
b = 5

ad = add(a, b)
su = sub(a, b)
mu = mul(a, b)
di = div(a, b)

 
print("{} + {} = {}".format(a, b, ad))
print("{} - {} = {}".format(a, b, su))
print("{} * {} = {}".format(a, b, mu))
print("{} / {} = {}".format(a, b, di))

