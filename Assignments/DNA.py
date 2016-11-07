#  File: DNA.py

#  Description: 

#  Student Name: Charles Lybrand

#  Student UT EID: cbl652

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: 10/23/2016

#  Date Last Modified: 10/24/2016

import string

def find_strands(dna1, dna2):
  '''
  Finds the largest substrings in two different strings
  '''
  strands = []
  seq_view = len(dna2)
  no_sub_strand = True
  # loop through until subsequences are only a character
  while(seq_view > 1 and no_sub_strand):
    # initialize starting index
    start = 0
    # loop through until view beyond string
    while(start + seq_view <= len(dna2)):
      # pick out a substrand
      sub_strand = dna2[start:start + seq_view]
      # find if the substrand exists in the other string
      if(dna1.find(sub_strand) != -1):
        strands.append(sub_strand)
        no_sub_strand = False
      # increment start
      start += 1
    # decrement seq_view
    seq_view -= 1

  return strands


def main():
  
  # Header
  print()
  print("Longest Common Sequences")
  print()

  dna_file = open("dna.txt", "r")

  # get the number of pairs
  n = int(dna_file.readline().strip())

  # cycle through all pairs of dna strands
  for i in range(n):
    
    # read in and clean up 2 lines at a time
    st1 = dna_file.readline()
    st2 = dna_file.readline()
    st1 = st1.strip()
    st1 = st1.upper()
    st2 = st2.strip()
    st2 = st2.upper()
    
    # order the two strings
    if (st1 > st2):
      dna1 = st1
      dna2 = st2
    else:
      dna1 = st2
      dna2 = st1

    # search for the largest strands
    print("Pair " + str(i+1) + " :", end=" ")
    strands = find_strands(dna1, dna2)
    # print results
    if (len(strands) > 0):
      for j in range(len(strands)):
        if(j < 1):
          print(strands[j])
        else:
          # print padding for cases with multiple sequences
          print( (7 + len(str(i)) )*" ", end = " ")
          print(strands[j])
    else:
      print("No Common Sequence Found")
      
    print()

  # close the file
  dna_file.close()

if __name__ == "__main__":
  main()