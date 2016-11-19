#  File: Spiral.py

#  Description: Returns the desired 3x3 section of a spiral of numbers

#  Student Name: Charles Lybrand

#  Student UT EID: cbl652

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: 11/17/2016

#  Date Last Modified: 11/18/2016

def inputs():
  '''
  prompt user for dimension and number in spiral
  '''

  # dimension
  print()
  dim = int(input("Enter dimension: "))
  # if even, add 1
  if(dim % 2 == 0):
  	dim += 1

  # number
  n = int(input("Enter number in spiral: "))

  return dim, n

def create_spiral(dim):
  '''
  Create and populate a number spiral
  '''
  spiral = []
  # create empty spiral of correct dimension
  for i in range(dim):
  	spiral.append([])
  	for j in range(dim):
  	  spiral[i].append([])

  # populate the spiral
  short = -1
  longer = dim
  i = -1
  j = dim
  n = dim**2
  while(n > 0):
  	# if on the top right corner change all of the deminsions
  	if(is_sqrt(n)):
  	  short += 1
  	  longer -= 1
  	  j -= 1
  	  i += 1

  	# if on the top row, proceed backwards
  	if(i == short and j > short):
  	  spiral[i][j] = n
  	  j -= 1

  	# if on bottom row, proceed forward
  	elif(i == longer and j < longer):
  	  spiral[i][j] = n
  	  j += 1

  	# if on l-column, proceed  forward
  	elif(j == short and i < longer):
  	  spiral[i][j] = n
  	  i += 1

  	# if on r-column, proceed backward
  	elif(j == longer and i > short):
  	  spiral[i][j] = n
  	  i -= 1

  	# if at 1
  	else:
  	  spiral[i][j] = n

  	# decrease number
  	n -= 1

  return spiral

def neighbor_numbers(dim, n):
  '''
  Given a spiral of numbers, and a number in the
  range and not on the edge, return a 3x3 spiral
  of all of the neighboring numbers
  '''

  # initialize spiral
  spiral = create_spiral(dim)

  # unoptimized search
  for i in range(dim):
  	for j in range(dim):
  	  # once the number is found return the 3x3 surrounding square
  	  if(spiral[i][j] == n):
  	  	# set i and j to be the top left corner
  	  	i -= 1
  	  	j -= 1
  	  	for k in range(3):
  	  	  print()
  	  	  for l in range(3):
  	  	  	print(spiral[i + k][j + l], end=" ")
  	  	# end the search
  	  	print("\n")
  	  	return


def is_sqrt(n):
  '''
  Check whether or not the number n is a perfect square of an odd integer
  '''
  # get the square root
  n = n**(1/2)

  # if n is odd and a perfect square
  return (int(n) % 2) and (n % 1 == 0.0)


def main():

  dim, n = inputs()
  dim_sqr = dim**2
  # if n is out of range, immediately tell the user and return
  if(n < 1 or n > dim_sqr):
  	print()
  	print("Number not in Range")
  	print()
  	return

  # if the number is on the outer edge, immediately tell the user and return
  if(n > (dim_sqr - 4*(dim - 1) ) ):
  	print()
  	print("Number on Outer Edge")
  	print()
  	return

  neighbor_numbers(dim, n)

if __name__ == "__main__":
  main()

