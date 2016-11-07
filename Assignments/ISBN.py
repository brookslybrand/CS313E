#  File: ISBN.py

#  Description: Varifies if numbers are viable ISBN numbers

#  Student Name: Charles Lybrand

#  Student UT EID: cbl652

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: 10/27/2016

#  Date Last Modified: 10/27/2016

def read_file():
  '''
  Reads in the txt file, cleans up the lines,
  passes it through the ISBN tester,
  then exports the results
  '''

  # open files
  infile = open("isbn.txt", "r")
  outfile = open("isbnOut.txt", "w")

  for line in infile:
  	# remove hyphens and new line characters
  	line_org = line.strip()
  	# before stripping hyphens, check if last value is incorrect
  	is_ISBN = (line_org[-1].isdigit() or line_org[-1] == 'x' or line_org[-1] == 'X')
  	# strip hyphens
  	line = line_org.replace("-","")

  	# initial varification tests
  	line_len = len(line)
  	is_ISBN = (line_len == 10) and is_ISBN

  	i = 0
  	line_arr = []
  	# varify all characters up to the last are digits and pass them into an array
  	while( (i < line_len - 1) and is_ISBN):
  	  ch = line[i]
  	  if(ch.isdigit()):
  	  	# convert to int
  	  	line_arr.append(int(ch))
  	  else:
  	  	is_ISBN = False
  	  # increment through the list
  	  i += 1

  	# convert and append last element
  	if(line[-1].upper() == "X" and is_ISBN):
  	  line_arr.append(10)
  	elif(is_ISBN):
  	  line_arr.append(int(line[-1]))

  	if(is_ISBN):
  	  is_ISBN = isISBN(line_arr)

  	if(is_ISBN):
  	  outfile.write(line_org + "  valid\n")
  	else:
  	  outfile.write(line_org + "  invalid\n")

  # close files
  infile.close()
  outfile.close()


def isISBN(arr):
  '''
  Test whether or not a 10 digit (last digit can be x or X)
  number could be an ISBN
  '''
  # get the first partial sum
  s1 = partialSum(arr)
  s2 = partialSum(s1)
  return (s2[-1] % 11 == 0)


def partialSum(arr):
  '''
  Compute the partial sum and return it as an array
  '''
  # better version of partial sum, introduced by Prof. Mitra
  for i in range(1, len(arr)):
    arr[i] = arr[i - 1] + arr[i]
  return arr

def main():
  
  read_file()

if __name__ == "__main__":
  main()