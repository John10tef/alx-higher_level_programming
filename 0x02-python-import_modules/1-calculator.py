#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10
b = 5

result_add = add(a, b)
result_sub = sub(a, b)
result_mul = mul(a, b)
result_div = div(a, b)

print("{0:d} + {1:d} = {2:d}".format(a, b, result_add))
print("{0:d} - {1:d} = {2:d}".format(a, b, result_sub))
print("{0:d} * {1:d} = {2:d}".format(a, b, result_mul))
print("{0:d} / {1:d} = {2:d}".format(a, b, result_div))
