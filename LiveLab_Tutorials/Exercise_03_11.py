#reverse the nubmers of the given input

def main():

  n = str(input("Enter an integer: "))

  for value in reversed(list(n)):
    print(value, end='')

  print("\n")

if __name__ == "__main__":
  main()