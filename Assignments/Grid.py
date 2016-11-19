
#  File: Grid.py

#  Description: Find the greatest product of 4 numbers in a row, column, or diagonal

#  Student Name: Charles Lybrand

#  Student UT EID: cbl652

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: 11/08/2016

#  Date Last Modified: 11/09/2016


# calculation based functions

def largest_product(a):
  '''
  Takes a 4*4 grid and finds the greatest product,
  across a row, column, or grid
  '''

  # hold the largest product
  largest_product = 0

  len_a = len(a)

  # product of each row
  for i in a:
  	prod = 1
  	for j in range(len_a):
  	  prod = i[j]*prod
  	  if (prod > largest_product):
  	  	largest_product = prod

  # product for each column
  for i in range(len_a):
  	prod = 1
  	for j in a:
  		prod = j[i]*prod
  		if (prod > largest_product):
  		  largest_product = prod

  # product for right diagonal
  prod = 1
  for i in range(len_a):
    prod = prod*a[i][i]
    if (prod > largest_product):
      largest_product = prod

  # product for left diagonal
  prod = 1
  for i in range(len_a):
    prod = prod*a[i][len_a-1-i]
    if (prod > largest_product):
      largest_product = prod


  return largest_product

def largest_product_per_grids(lines, dim, sub):
  '''
  calculate the largest product per sub*sub grids in sub lines
  '''

  # initialize the maximum product
  max_prod = 0;

  # iterate up to the dim - sub column
  for j in range(dim + 1 - sub):
  	grid = []

  	# iterate over all lines
  	for i in range(len(lines)):
  	  grid.append(lines[i][j:j+sub])
  	
  	# find if there is a larger product in the sub*sub grid
  	new_prod = largest_product(grid)
  	if (new_prod > max_prod):
  	  max_prod = new_prod

  return max_prod

# file-related functions

def clean_line(line):
  '''
  Takes in a string of ints seperated by spaces and returns an array of ints
  '''
  # get the string versions of the ints in an array
  line = line.strip()
  line = line.split(" ")

  # convert all strings to ints
  ints = []
  for ch in line:
  	ints.append(int(ch))

  # return the array of ints
  return ints


def read_file(sub):
  '''
  read the file and find the largest product for each sub*sub grid in the total grid
  '''

  infile = open("grid.txt", "r")
  dim = infile.readline()
  dim = int(dim.strip())

  # select the first sub - 1 lines of the file
  lines = []
  while(len(lines) < sub - 1):
  	# read the line
  	line = infile.readline()
  	# get the ints as an array and append them to the lines array
  	lines.append(clean_line(line))

  # counter for when the end of the file has been reached
  line_start = sub

  # maximum product variable
  max_prod = 0;

  # go through every sub*sub grid in the larger grid and preform calculations
  while(line_start < dim):
  	
  	# read the next line
  	line = infile.readline()
  	# get the ints as an array and append them to the lines array
  	lines.append(clean_line(line))

  	# go through the sub*sub grids in the current sub lines
  	new_prod = largest_product_per_grids(lines, dim, sub)
  	if(new_prod > max_prod):
  	  max_prod = new_prod

    # remove the first line
  	lines.pop(0)

    # increment the start of the line to indicate when the while loop should terminate
  	line_start += 1

  return max_prod

  infile.close()

def main():

  print()
  print("The greatest product is %s." % read_file(4))
  print()

if __name__ == "__main__":
	main()