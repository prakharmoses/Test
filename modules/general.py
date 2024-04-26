import math

def sigmoid(x):
  dem = math.exp(x)
  return 1/dem

def add(a):
  sum = 0
  for i in a:
    sum += i
  return sum

def complex(x, y):
  return (x.real + y.real) + (x.img + y.img)*j
