# NWS windchill formula

def main():

  # prompt the user to enter a 4 digit integer
  myint_len = 0;
  while ( myint_len != 4):
    myint = int(input("Enter an integer: "))
    myint_str = str(myint)
    myint_len = len(myint_str)

  # display the nnumber in reverse order
  for i in range(0, myint_len):
    print( myint_str[ myint_len - (i + 1) ] )
    


if __name__ == '__main__':
    main()