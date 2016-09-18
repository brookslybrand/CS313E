# print a pyramid of n lines from j-to-1-to-j with appropriate padding

def padding(pad):
  '''
  Add the padding of two spaces
  '''
  for x in range(0, pad):
    print(" ", end="")
    
def line(nMax, n):
  '''
  Print a single line given the number inputed and the line number
  '''
    
  padding(nMax - n) # add padding
    
  for x in range(n, 1, -1): # decreasing numbers to 1
    print(x, end=" ")

  for x in range(1, n + 1): # increasing numbers to n
    print(x, end=" ")
    
  print("\n") # print a new line
  

def main():
  n = 0;
  while(n < 1 or n > 15):
    n = int(input("Enter the number of lines: ")) # user input
    
  for x in range(1, n + 1): # for loop to print all lines
    line(n, x)
    
if __name__ == "__main__":
  main()