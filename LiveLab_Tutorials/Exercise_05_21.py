# pyramid of multiples of 2s

def padding(pad):
  for x in range(0, pad):
    print("   ", end="")
    
def line(nMax, n):
    
  padding(nMax - n)

  for x in range(0, n - 1):
    print(2**x, end="  ")
    
  for x in range(n - 1, -1, -1):
    print(2**x, end="  ")
    
  print("\n")
  

def main():
  
  for x in range(1, 8 + 1):
    line(8, x)
    
if __name__ == "__main__":
  main()

