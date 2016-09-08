# Compound Value over six months with constant monthly deposit
''' The balance function recursively calls itself until months is zero.
Keyword arguments have been used. This is similar to passing an
association to a function in MMa. If no values are present, they keyword
takes on the default value.

The code assumes that the deposit is reoccuring each month.
'''
def balance(deposit=0, start_balance=0, rate=(1 + .05/12), months=6):
    '''Recursive function to compute compounding interest.'''
    if not months:
        return start_balance
    d = deposit
    b = start_balance
    r = rate
    m = months
    return balance(deposit=d, start_balance=(d + b) * r, months=m - 1)

#print( balance(deposit=100) )


def main():

  # prompt for monthly deposit
  #dep = float(input("Enter the monthly saving amount: "))
  dep = 100.0

  rate = 1 + 0.05/12

  #compound for six months
  balance = 0
  i = 0
  while i < 6:
    balance = (dep + balance)*(rate)
    i = i + 1




  # print result
  print("After the sixth month, the account value is", balance)







if __name__ == '__main__':
    main()
