
# coding: utf-8

# In[15]:

# find all of the perfect numbers

import math

def find_factors(n):
  '''
  finds all of the factors for a given number n without n itself
  '''
  f = []
  for i in range(1, int(math.sqrt(n)) + 1):
    if (n % i == 0):
      if(i != n//i):
        f.append(i)
        f.append(n//i)
      else:
        f.append(i)
        
  f.remove(n)
  return f

def main():
  '''
  find all of the perfect numbers from 1 to 10,000
  '''
    
  perfs = []
  for x in range(1, 10001):
    if(sum(find_factors(x)) == x):
      perfs.append(x)
    
  print(perfs)
    
if __name__ == "__main__":
  main()


# In[ ]:



