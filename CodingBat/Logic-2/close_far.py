
# coding: utf-8

# In[9]:

def close_far(a, b, c):
  '''
  return True if b or c is within 1 of a, and while the other is 2 or more from the rest 
  '''
  ab_dif = abs(b - a)
  ac_dif = abs(c - a)
  bc_dif = abs(b - c)

  if(ab_dif <= 1):
    return (ac_dif >=2 and bc_dif >= 2)
  elif(ac_dif <= 1):
    return (ab_dif >=2 and bc_dif >= 2)
  else:
    return False

