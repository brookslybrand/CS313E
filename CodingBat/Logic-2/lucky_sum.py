def lucky_sum(a, b, c):
  '''
  sum the numbers expect for an 13s and numbers following a of in the list
  '''
  ints = [a, b, c]
  sum = 0
  for x in ints:
    if (x == 13):
      break
    else:
      sum = sum + x
        
  return sum

