# Print two estimates of pi

def main():
  pi1 = 4 * ( 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 )
  pi2 = 4 * ( 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + 1/13 - 1/15 )
  print(pi1)
  print(pi2)
    
if __name__ == '__main__':
    main()