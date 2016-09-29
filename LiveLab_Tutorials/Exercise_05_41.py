def main():
  '''
  keep reading in imput till 0, print largest number and occurances
  '''
  # keep prompting until user puts a zerp
  user_input = int(input("Enter a number (0: for end of input): "))
  max = 0
  count = 0
  while (user_input):
    user_input = int(input("Enter a number (0: for end of input): "))
    
    if (user_input > max):
      max = user_input
      count = 1
    elif (user_input == max):
      count += 1
    
  print("The largest number is", max)
  print("The occurence count of the largest nubmer is", count)
        
        
if __name__ == "__main__":
  main()

