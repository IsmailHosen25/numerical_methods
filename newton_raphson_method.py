def f(x):
  return x**2 - 16

def fPrime(x):
  return 2*x


'''
#Use differentiation module from sympy

import sympy as sym
import math

def f(x):
  return x**3 + x**2 + 3*x + 2

def fPrime(x):
  xSymbol = sym.symbols('x')
  diffStr = str(sym.diff(f(xSymbol),xSymbol))
  return (eval(diffStr))
print(fPrime(2))

'''



b = 10

i = 0
while i < 9:
  a = b - (f(b) / fPrime(b))
  print(a)
  #print(b, f(b)/ fPrime(b))
  b = a
  i = i + 1