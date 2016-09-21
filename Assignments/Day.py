# 2/29/2000

#  File: Day.py

#  Description: Calulate the day of the week for a given year, month, and day

#  Student Name: Charles Lybrand

#  Student UT EID: cbl652

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: 09/20/2016

#  Date Last Modified: 09/20/2016


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
  while ( not( 1 <= m <= 12 ) ):
    m = int(input("Enter month: "))

  d = 0
  while ( not( 1 <= d <= month_days(m - 1, y) ) ):
    d = int(input("Enter day: "))

  return [y, m, d]


def inputs_convert():
  '''
  Convert the inputs into a b c and d necessary for the Zeller algorithm
  '''

  date = inputs()

  # Use tuple unpacking
  # y, m, b = date
  y = date[0]
  m = date[1]
  b = date[2]

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

# Updated signature for compute_day; accepts list as args
# def compute_day(*args):
#     a, b, c, d = args
def compute_day(a, b, c, d):
  '''
  Zeller's Algorithm for computing the day of the week
  '''

  abcd = inputs_convert

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

  abcd = inputs_convert()

  # Indexings over the days gets tiresome and hard to read. Why not pass a list?
  # To pass as a list, the signature of compute_day needs changed to a star argument.
  # Star-args are similar to a mathematica f[x__];
  # day = compute_day(abcd)
  day = compute_day(abcd[0], abcd[1], abcd[2], abcd[3])


  # Time to talk about string formatting. You're using a JS style concatenation.
  # Think about build string templates to populate
  # print( 'The day is %s.' % day )
  print()
  print("The day is", day + ".")


if __name__ == "__main__":
  main()
