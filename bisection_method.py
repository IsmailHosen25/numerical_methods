def f(x):
  return x**2 - 9

#f(x)= x^2 - 5

def getRoot():
  a = 0
  b = 10

  i = 0
  while( i < 30):
    c = (a + b) / 2.0
    print(c)

    if f(c) * f(a) < 0:
      b = c

    if f(c) * f(b) < 0:
      a = c

    i = i + 1
getRoot()