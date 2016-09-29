def main():
  '''
  find if point is in the rectangle 10x5
  '''

  # get the point of the rectangle from the user
  user_input = input("Enter a point with two coordinates: ").split(", ")
  x, y = [float(x) for x in user_input]
  
  # test whether or not the point is in the rectangle
  if (abs(x) <= 5 and abs(y) <= 2.5):
    print("Point (%f, %f) is in the rectangle" % (x, y))
  else:
    print("Point (%f, %f) is not in the rectangle" % (x, y))
      
if __name__ == "__main__":
  main()