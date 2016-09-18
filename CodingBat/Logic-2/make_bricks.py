def make_bricks(small, big, goal):
  '''
  Find out if we can make the row of bricks goal inches long,
  given that big bricks are 5 inches, and smalls are 1
  '''

  big_need = goal // 5  
    
  if (big >= big_need):
    return (goal % 5 <= small)
  else:
    return (5*big + small >= goal)

