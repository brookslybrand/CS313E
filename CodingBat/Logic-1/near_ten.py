
# coding: utf-8

# In[147]:

def near_ten(num):
  '''
  return True if num is within 2 of a multiple of 10
  '''
  mod = num % 10
  return ( (mod <= 2) or (8 <= mod <= 9) )

