def caught_speeding(speed, is_birthday):
  '''
  measure whether or not someone is speeding and what ticket they should recieve if so
  '''

  bonus = 0
  if(is_birthday):
    bonus = 5

  if (speed <= 60 + bonus):
    return 0
  elif (speed <= 80 + bonus):
    return 1
  else:
    return 2

