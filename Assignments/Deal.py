# File: Deal.py

# Description: Varify Marilyn vos Savant's strategy for "Lets Make a Deal"

# Student Name: Charles Lybrand

# Student UT EID: cbl652

# Course Name: CS 303E

# Unique Number: 51200

# Date Created: 10/19/2016

# Date Last Modified: 10/19/2016

import random
import string

def plays_input():
  '''
  Prompt the user for how many times they want to play
  '''
  print()
  plays = int(input("Enter number of times you want to play: "))
  print()
  print(
  	str("Prize").center(10),
  	str("Guess").center(10),
  	str("View").center(10),
  	str("New Guess").center(10)
  )

  return plays

def view_door(prize, guess):
  '''
  Given the prize and the guess, return the door Monty opens
  '''
  dif = prize - guess
  if(dif):
  	return 6 - prize - guess
  else:
  	return prize % 3 + 1


def game():
  '''
  Simulation of the Lets Make a Deal with switch
  '''

  # randomly generate the prize and the guess	
  prize = random.randint(1,3)
  guess = random.randint(1,3)

  # calculate the revealed door and the guess after switching
  view = view_door(prize, guess)
  new_guess = 6 - guess - view

  # print results
  print(
  	str(prize).center(10),
  	str(guess).center(10),
  	str(view).center(10),
  	str(new_guess).center(10)
  )
  # return if the switched guess was right
  return prize == new_guess


def main():
  '''
  Prompt user for plays
  Simulate game 'plays' times
  Display win to loss probability
  '''
  
  # get the number of plays
  plays = plays_input()

  # play the game 'plays' times and keep count of the wins
  wins = 0
  for x in range(plays):
  	
  	result = game()
  	if(result):
  	  wins += 1

  win_prob = wins/plays
  lose_prob = 1 - win_prob

  print()
  print("Probability of winning if you switch =", "%.2f" % (win_prob))
  print("Probability of winning if you do not switch =", "%.2f" % (lose_prob))
  print()



if __name__ == "__main__":
  main()