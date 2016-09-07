# Compound Value over six months with constant monthly deposit

def main():

  # prompt for monthly deposit
  dep = float(input("Enter the monthly saving amount: "))

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