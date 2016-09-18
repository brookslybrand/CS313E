def make_chocolate(small, big, goal):
  '''
  return how many small bars are needed, -1 if impossible
  '''
  big_need = goal // 5
  small_need = goal % 5  
    
  if ( big >= big_need):
    if (small >= small_need ):
      return small_need
    else:
      return -1
  else:
    small_need = 5*(big_need - big) + small_need
    if ( small >= small_need ):
      return small_need
    else:
      return -1

