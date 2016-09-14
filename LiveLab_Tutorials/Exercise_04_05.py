# give a future date

def main():

  # inputs
  day = int(input("Enter today's day: "))
  future_days = int(input("Enter the number of days elapsed since today: "))

  # days of the week
  week_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

  print("Today is", week_days[day], "and the future day is", week_days[ (day + future_days) % 7 ])
    
if __name__ == "__main__":
  main()