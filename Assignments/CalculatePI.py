#  File: CalculatePI.py

#  Description: Calculate the value of PI using a simulation of random "dart throws"

#  Student Name: Charles

#  Student UT EID: cbl652

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: 10/10/2016

#  Date Last Modified: 10/12/2016

import math
import random

def num_digits(num):
  '''
  return the number of digits in num
  
  used in padding_num
  '''
  
  digits = 0
  while (num > 0):
  	num = num // 10
  	digits += 1

  return digits


def padding_num(num):
  '''
  Adds padding up to 10 spaces (assuming that there is at least one digit)
  '''

  padding = 11 - num_digits(num) # total characters is always 11
  pad_count = 0
  while (pad_count < padding):
    print(" ", end="")
    pad_count += 1


def computePi(numThrows):
  '''
  Simulates random dart throws and calculates PI from the results
  '''
  
  # ouput number of random numbers
  print("num =", numThrows, end = "")

  # Add padding to output
  padding_num(numThrows)

  # initialize variables to count the number of throws in the circle and outside the circle
  throws = 0
  circle = 0
  # generate a point for each 'throw'
  while (throws < numThrows):
  	# randomly generate the point on the 'dart board'
  	xPos = random.uniform (-1.0, 1.0)
  	yPos = random.uniform (-1.0, 1.0)
  	# add to circle if dart 'hit'
  	if(math.hypot(xPos, yPos) < 1): # the radius of the circle is 1
  	  circle += 1
  	# update counter
  	throws += 1

  # calculated value of PI
  calc_PI = 4 * (circle/throws)
  # output calculated value of PI
  print("Calculated PI = %.6f" % (calc_PI), end ="   ")

  # difference between real PI and calc_PI
  dif = calc_PI - math.pi
  # output difference, adding '+' if need be
  print ("Difference = %+-.6f" % dif )


def main():
  '''
  Compute PI based on a random generator
  Print the results and the difference from the real number pi
  '''

  # program header
  print()
  print("Computation of PI using Random Numbers")
  print()

  # actual computation

  # init numThrows
  numThrows = 100
  # print the results for each factor of 10 number of throws
  while (numThrows <= 10000000):
  # print the results and increment
    computePi(numThrows)
    numThrows = numThrows * 10

  # program footer
  print()
  print("Difference = Calculate PI - math.pi")
  print()


if __name__ == "__main__":
  main()