def squirrel_play(temp, is_summer):
  '''
  Find out whether the squirrels play or not based on temperature and season
  '''
  return ( ( temp >= 60 ) and ( (temp <= 90) or (is_summer and temp <= 100 ) ) )

