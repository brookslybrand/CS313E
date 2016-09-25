# 2/29/2000

#  File: Day.py

#  Description: Calulate the day of the week for a given year, month, and day

#  Student Name: Charles Lybrand

#  Student UT EID: cbl652

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: 09/20/2016

#  Date Last Modified: 09/22/2016


def is_leap(y):
  '''
  Determine if the current year is a leap year
  '''
  return ( y % 4 == 0 and ( y % 400 == 0 or y % 100 != 0 ) )


def month_days(m, y):
  '''
  Return the days in the given month
  '''

  monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

  # handle leap year exception
  if( m == 1 and is_leap(y) ):
    return 29
  else:
    return monthDays[m]

def inputs():
  '''
  Get the year, month, and day from the user
  '''

  y = 0
  while ( not ( 1900 <= y <= 2100) ):
    y = int(input("Enter year: "))

  m = 0
  while ( not ( 1 <= m <= 12 ) ):
    m = int(input("Enter month: "))

  d = 0
  while ( not ( 1 <= d <= month_days(m - 1, y) ) ):
    d = int(input("Enter day: "))

  return [y, m, d]


def inputs_convert():
  '''
  Convert the inputs into a b c and d which are used for the Zeller algorithm
  '''

  y, m, b = inputs()

  # adjust months
  if ( m < 3):
    a = 10 + m
    y = y - 1
  else:
    a = m - 2
    y = y

  # get year and century
  c = y % 100
  d = y // 100

  return [a, b, c, d]


def compute_day(*args):
  '''
  Zeller's Algorithm for computing the day of the week
  '''
  
  a, b, c, d = args

  # algorithm

  w = (13 * a - 1 ) // 5

  x = c // 4

  y = d // 4

  z = w + x + y + b + c - 2 * d

  r = z % 7

  r = (r + 7) % 7

  # day index
  days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

  return days[r]


def main():
  '''
  Compute the day
  '''

  day = compute_day(*inputs_convert())

  print()
  print("The day is %s." % day)


if __name__ == "__main__":
  main()
