def main():
  '''
  calculate the future investment value
  '''
  
  # inputs
  i = float (input ("Enter investment amount: "))
  ir = float (input ("Enter annual interest rate: "))/(100*12)
  m = 12*int (input ("Enter number of years: "))
  
  # future investment value formula
  v = i*( (1 + ir )**m)

  print("Accumulate value is",v)
    
if __name__ == "__main__":
  main()