import numpy as np

def add_list(a: np.array, b: np.array) -> np.array:
  return a+b

def multiply_const(a: np.array, b: int) -> np.array:
  return b*a

def square(x: np.array) -> np.array:
  return x**2

def root_nth_power(p: np.array, m: int) -> np.array:
  return p**(m)
