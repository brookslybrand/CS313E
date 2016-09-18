# for some reason CodingBat would not allow me to use round, so I made the dirtier version below

def round10(n):
  '''
  round a multiple of 10
  '''
  if (n % 10 >= 5):
    return ( (n + 10) // 10 )* 10
  else:
    return ( (n) // 10 )* 10

def round_sum(a, b, c):
  '''
  sums all the numbers and round to nearest 10
  '''
  return round10(a) + round10(b) + round10(c)