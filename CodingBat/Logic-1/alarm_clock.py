
def alarm_clock(day, vacation):
  '''
  check if and when the alarm should be set  
  '''

  if ( (day - 1) // 5): #it's the weekend
    if (vacation):
      return "off"
    else:
      return "10:00"
  else:
    if (vacation):
      return "10:00"
    else:
      return "7:00"

