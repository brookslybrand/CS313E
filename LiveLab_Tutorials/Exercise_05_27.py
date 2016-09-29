def main():
  '''
  compute values of pi
  '''

  # formula
  pi = lambda x: 4*(((-1)**(x+1))/(2*x - 1))
 
  for i in range(10000, 100001, 10000):
    sum = 0
    for j in range(1, i + 1):
      sum += pi(j)
    print(sum)
      
if __name__ == "__main__":
  main()

