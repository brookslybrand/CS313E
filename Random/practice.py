def main():
  
  '''
  # init num
  num = 0;
  num_largest = 0;
  num_s_largest = 0;

  # keep prompting for num until num == -1
  while(num != -1):
    num = int(input("Enter a number (-1 to cancel): "))
    if(num > num_largest):
      num_s_largest = num_largest
      num_largest = num
  print(num_s_largest, "is the second largest number.")
  '''
  
  lastL = 0
  sumL = 0
  lastR = 0
  sumR = 0
  last_house = 10000

  while(lastR <= last_house):
    lastL += 1
    sumL += lastL
    lastR = lastL + 2
    sumR = lastR
    while(sumR < sumL):
      lastR += 1
      sumR += lastR
    if(sumL == sumR):
      lucky = lastL + 1
      print(lucky, lastR)



if __name__ == "__main__":
  main()