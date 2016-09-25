#  File: Hailstone.py

#  Description: Find the largest hailstone sequence and number in a given range

#  Student Name: Charles Lybrand

#  Student UT EID: cbl652

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: 09/23/2016

#  Date Last Modified: 09/25/2016


def main():
    
  # initialize variables used throughout
  a = 0
  b = 0
  num = 0
  cycle_largest = 0
  cycle = 0
  
  # check and keep prompting user for input until they are both positive and b is greater than a
  while( a <= 0 or b <= a ):
    a = int(input("Enter starting number of the range: "))
    b = int(input("\nEnter ending number of the range: "))
    
  # run through all numbers in the range of a to b inclusive
  for n in range(a, b + 1):
    # save the number before mutating it
    num_org = n

    # preform the conjecture until n = 1
    while(n > 1):

      if (n % 2):
        n = n*3 + 1
      else:
        n = n // 2

      cycle += 1

    # check if the cycle is greater than the largest cycle thus far
    if ( cycle >= cycle_largest ):
      num = num_org
      cycle_largest = cycle
    
    # reset the cycle count
    cycle = 0

        
  print('\nThe number %s has the longest cycle length of %s.\n' % (num, cycle_largest))
  

if __name__ == "__main__":
  main()