def date_fashion(you, date):
  '''
  Find out whether or not you and your date can get a table
  '''
  if ( you <= 2 or date <= 2):
    return 0
  elif ( you >= 8 or date >= 8):
    return 2
  else:
    return 1

