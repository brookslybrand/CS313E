#  File: EasterSunday.py

#  Description: Calculate the date for Easter Sunday since 1583 using Carl Friedrich Gauss's algorithm

#  Student Name: Charles Lybrand

#  Student UT EID: cbl652

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: 09/07/2016

#  Date Last Modified: 09/09/2016

def main():

  # get year from user and convert it to an int
  y = int(input("Enter year: "))

  # compute a
  a = y % 19

  # compute b and c
  b = y // 100
  c = y % 100

  # compute d and e
  d = b // 4
  e = b % 4

  # compute g
  g = ( ( 8 * b ) + 13) // 25

  # compute h
  h = ( ( 19 * a ) + b - d - g + 15 ) % 30

  # compute j and k
  j = c // 4
  k = c % 4

  # compute m
  m = ( a + ( 11 * h )) // 319

  # compute r
  r = ( ( 2 * e ) + ( 2 * j ) - k - h + m + 32 ) % 7

  # compute n
  n = ( h - m + r + 90 ) // 25

  # compute p
  p = ( h - m + r + n + 19 ) % 32
    
  # index of the months
  months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

  # print a new line
  print(" ")
    
  # return Easter Sunday for year y
  print( "In", y, "Easter Sunday is on", p, months[n - 1] + "." )
    
# run the algorithm
if __name__ == '__main__':
    main()