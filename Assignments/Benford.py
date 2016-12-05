#  File: Benford.py

#  Description: Varify that Benford's Law holds for the 2009 census data

#  Student Name: Charles Lybrand

#  Student UT EID: cbl652

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: 11/19/2016

#  Date Last Modified: 11/19/2016


def main():
  # create an empty dictionary
  pop_freq = {}

  # initialize the dictionary
  pop_freq ['1'] = 0
  pop_freq ['2'] = 0
  pop_freq ['3'] = 0
  pop_freq ['4'] = 0
  pop_freq ['5'] = 0
  pop_freq ['6'] = 0
  pop_freq ['7'] = 0
  pop_freq ['8'] = 0
  pop_freq ['9'] = 0

  # open file for reading
  in_file = open ("./Census_2009.txt", "r")

  # read the header and ignore
  header = in_file.readline()

  # read subsequent lines
  for line in in_file:
    line = line.strip()
    pop_data = line.split()
    # get the last element that is the population number
    pop_num = pop_data[-1]
    # get the first digit in the population number
    pop_num_first = pop_num[0]

    # make entries in the dictionary
    pop_freq[pop_num_first] += 1

  # close the file
  in_file.close()

  # get the total number of entries
  total_pop = sum(pop_freq.values())

  # write the header
  print()
  print("Digit\tCount\t%")

  # convert raw number to frequency
  for i in range(1, 10):
  	# get the count and frequency
  	count = pop_freq[str(i)]
  	freq = 100*(count/total_pop)
  	# write out the result
  	print( "%s\t%s\t%0.1f" % (i, count, freq) )

  print()
  
main()