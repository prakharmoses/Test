# Contains main code
import pandas as pd
import numpy as np

class Dog:
  attr1 = "mammal"
  attr2 = "dog"

  # A sample method
  def fun(self):
      print("I'm a", self.attr1)
      print("I'm a", self.attr2)

def total_age(df):
  sum = 0
  for col, colitems in df.itercolumns():
    if col == "Age":
      for val in colitems:
        sum += val;
  return sum
      

a = np.arays([[1,2,3,5,6,9,8]])
b = {"Name": ["Vishu", "Kunal", "Tashu", "Am", "KRTK"], "Age": [20, 21, 22, 19, 19.5], "Grade": ["S", "S", "S", "A", "A"]}
df = pd.DataFrame(b)
print(df)
print(total_age(df))
