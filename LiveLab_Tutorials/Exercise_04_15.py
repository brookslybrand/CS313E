import random

def main():
  '''
  find how much the user wins from the lottery
  '''

  # generate random 3 digit number
  lottery = random.randint(100, 999)

  # recive a 3 digit number from the user
  guess = int(input("Enter your lottery pick (three digits): "))
  
  # get the individual digits for the lotter number
  lotteryDigit1 = lottery // 100
  lotteryDigit2 = (lottery - lotteryDigit1*100) // 10
  lotteryDigit3 = lottery % 10
  # put them in an array
  lottery_array = [lotteryDigit1, lotteryDigit2, lotteryDigit3]

  # get the individual digits for the guess number
  guessDigit1 = guess // 100
  guessDigit2 = (guess - guessDigit1*100) // 10 
  guessDigit3 = guess % 10
  # put them in an array
  guess_array = [guessDigit1, guessDigit2, guessDigit3]
    
  # print the random number
  print("The lottery number is", lottery)
  
  # count the number of same digits
  count = 0;
  for i in guess_array:
    for j in lottery_array:
      if (i == j):
        count += 1
        lottery_array.remove(j)
        break

  if (guess == lottery): # instant win
    print("Exact match: you win $10,000")
  elif (count == 3): # three digits match
    print("Match all digits: you win $3,000")
  elif (count >= 1): # at least one digit matches
    print("Match one digit: you win $1,000")
  else:
    print("Sorry, no match")
  
  
    
if __name__ == "__main__":
  main()

