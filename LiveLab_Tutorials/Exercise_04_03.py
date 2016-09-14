# Solving 2*2 linear problems using Cramer's rule

def main():

  # input six numbers
  a, b, c, d, e, f = input("Enter a, b, c, d, e, f: ").split(", ")
  
  # convert to floats
  a = float(a)
  b = float(b)
  c = float(c)
  d = float(d)
  e = float(e)
  f = float(f)
   
  # make sure the numerator isn't zero, then preform calculations
  if (a*d - b*c):
    x = (e*d - b*f)/(a*d - b*c)
    y = (a*f - e*c)/(a*d - b*c)
    print("x is", x, "and y is", y)
  else:
    print("The equation has no solution")
    
    
if __name__ == "__main__":
  main()