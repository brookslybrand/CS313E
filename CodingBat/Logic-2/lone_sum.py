def lone_sum(a, b, c):
  '''
  sum the numbers that are not duplicates
  '''
  ints = [a, b, c]
  sum = 0
  for x in ints:
    if (ints.count(x) == 1):
        sum = sum + x
        
  return sum

