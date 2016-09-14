def sorta_sum(a, b):
  '''
  return the sum for two integers, with the exception of 20 returned for anything between 10-19
  '''
  sum = a + b
  if (10 <= sum <= 19):
    return 20
  else:
    return sum

