#  File: CreditCard.py

#  Description: Checks if a credit card number is valid or not and attempts to identify

#  Student Name: Charles Lybrand

#  Student UT EID: cbl652

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: 11/09/2016

#  Date Last Modified: 11/14/2016


def is_valid(a):
  '''
  Luhn's test for testing the validity of a credit card
  '''
  a.reverse()
  for i in range(len(a)):
  	# if the digit is odd...
  	if(i % 2 != 0):
  	  num = a[i]
  	  # mutliply by two
  	  num *= 2
  	  # sum the digits (either 1 or 2 digits)
  	  num = num//10 + num%10
  	  #replace original number with new number
  	  a[i] = num

  # if sum is divisable by 10 it is valid
  return sum(a)%10

def cc_type (cc_num):

  # American Express
  if(cc_num[:2] == '34' or cc_num[:2] == '37'):
  	return "Valid American Express credit card number"

  # Discover
  if(cc_num == '6011' or cc_num[:3] == '644' or cc_num[:2] == '65'):
  	return "Valid Discover credit card number"

  # MasterCard
  if(cc_num[0] == '5' and (int(cc_num[1]) - 5) <= 0):
  	return "Valid MasterCard credit card number"
  
  # Visa
  if(cc_num[0] == '4'):
  	return "Valid Visa credit card number"

  # return a blank string if cannot identify the card
  return "Valid credit card number"

def main():
  
  # prompt the user for their credit card number
  print()
  cn = input("Enter 15 or 16-digit credit card number: ")
  print()

  # check if 15 or 16 digits long
  if(len(cn) != 15 and len(cn) != 16):
  	# print error and escape program
  	print("Not a 15 or 16-digit number")
  	print()
  	return
  
  # turn the number into an array of ints
  c_digits = []
  for i in cn:
    c_digits.append(int(i))

  # make a copy of the cc number
  cc_num = cn[:4]

  # test if the credit card is valid
  # 4432333884138343
  if(is_valid(c_digits)):
  	print("Invalid credit card number")
  	print()
  	return

  # print the credit card type
  print(cc_type(cc_num))
  print()


if __name__ == "__main__":
  main()
