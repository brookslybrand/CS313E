
# coding: utf-8

# In[129]:

def in1to10(n, outside_mode):
  '''
  return True if between 1 and 10 inclusive, or
  outside those numbers if outside_mode = True
  '''

  return ( (not outside_mode and 1 <= n <= 10) or (outside_mode and (n <= 1 or n >= 10) ) )

