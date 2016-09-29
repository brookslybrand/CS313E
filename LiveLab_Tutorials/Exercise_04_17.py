import random

def main():
  '''
  simulate rock paper scissors
  '''

  # generate random 3 digit number
  comp_choice = random.randint(0, 2)

  # recive a 3 digit number from the user
  user_choice = int(input("scissor (0), rock (1), paper (2): "))
  
  # rock, paper, scissors index
  rps = ["scissors", "rock", "paper"]

  if (comp_choice == user_choice):
    print("The computer is %s. You are %s too. It is a draw." % (rps[comp_choice], rps[user_choice]) )
  elif((user_choice == 0 and comp_choice == 2)
    or (user_choice == 1 and comp_choice == 0)
    or (user_choice == 2 and comp_choice == 3)):
    print("The computer is %s. You are %s. You won." % (rps[comp_choice], rps[user_choice]) )
  else:
    print("The computer is %s. You are %s. You lost." % (rps[comp_choice], rps[user_choice]) )
  
    
if __name__ == "__main__":
  main()