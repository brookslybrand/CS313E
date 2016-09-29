def main():
  '''
  all possible combinations of integers 1 through 7
  '''
  
  count = 0
  for i in range (1, 8):
    for j in range (i + 1, 8):
      print (i,j)
      count += 1
        
  print("The total number of all combinations is", count)
        
if __name__ == "__main__":
  main()