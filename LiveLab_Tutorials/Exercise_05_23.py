def main():
  '''
  compare loans and interests
  '''

  # get the loan amount and number of years
  loan = int(input("Loan amount: "))
  yrs = int(input("Number of years: "))
  
  print("Interest Rate    Monthly Payment     Total Payment")
    
  for x in range(5000, 8125, 125):
    x = x / 1000
    print(format(x, '.3f') + "%", end="            ")
   
    # calculate monthly interest
    mi = x/(12*100)
    # calculate monthly payment
    mp = loan*(mi/(1-(1 + mi)**(-yrs*12)))
    print(format(mp, '.2f'), end="            ")
    
    # calculate annual payment
    ap = mp*12*yrs
    print(format(ap, '.2f'))
      
if __name__ == "__main__":
  main()