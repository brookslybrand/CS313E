#  File: Goldbach.py

#  Description: Test and show all examples of the Goldbach conjecture for a givin range of numbers

#  Student Name: Charles Lybrand

#  Student UT EID: cbl652

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: 10/07/2016

#  Date Last Modified: 10/10/2016

def get_input():
  '''
  Get the lower and upper limit from the user
  '''
  
  # init lower and upper limit to start the while loop
  l_limit = 0
  u_limit = 0
  
  # while loop to keep prompting for the inputs
  while (
  	      (l_limit < 4) # lower limit must be greater than or equal to 4
  	      or (l_limit >= u_limit) # lower limit must be less than upper limit
  	      or (l_limit % 2 == 1 or u_limit % 2 == 1) # both numbers must be even
  	    ):
    # user inputs
  	l_limit = int( input( "Enter the lower limit: " ) )
  	u_limit = int( input( "Enter the upper limit: " ) )

  return (l_limit, u_limit)

def is_prime(num):
  '''
  Check if a single number is a prime number or not (1 is not considered prime)
  '''

  # initiate variables
  divisor = 2
  limit = int(num**0.5) + 1
  isPrime =  num > 1

  while( (divisor < limit) and isPrime):
    
    if(num % divisor == 0):
      isPrime = False
    
    divisor += 1

  return isPrime

def goldback_Conj(num):
  '''
  Produce the solutions to the Goldback Conjecture for a single even number
  '''

  # only go to half the numbers so as not to re-calculate numbers
  limit = num // 2 + 1
  
  # find all of the sums of primes
  for x in range(2, limit):
    # get the complement of x
  	x_comp = num - x
  	if( is_prime(x) and is_prime(x_comp) ):
  	  print( '= %s + %s' % ( str(x), str(x_comp) ), end = " " )

def goldback_range(l_limit, u_limit):
  '''
  Produce the Goldback Conjecture solutions over a range of numbers
  '''

  for x in range(l_limit, u_limit + 1, 2):
    print(str(x), end=" ")
    goldback_Conj(x)
    print()

def main():
  '''
  Gather inputs and ouput the results
  '''

  # get the lower and upper limit
  l_limit, u_limit = get_input()

  goldback_range(l_limit, u_limit)
  

if __name__ == "__main__":
  main()