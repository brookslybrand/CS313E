def fix_teen(n):
  '''
  converts teens into 0s, except 15 and 16
  '''
  if(13 <= n <= 19 and ( ( n is not 15 ) and  ( n is not 16 ) ) ):
    return 0
  else:
    return n

def no_teen_sum(a, b, c):
  '''
  sums all the numbers, except teens that aren't 15 or 16
  '''
  ints = [a, b, c]
  sum = 0
  for x in ints:
    sum = sum + fix_teen(x)
        
  return sum

