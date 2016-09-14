# calculate the area of a pentagon given the length from the center to one vertex

import math

def main():
  r = float(input("Enter the length from the center to a vertex: "))

  s = 2 * r * math.sin(math.pi/5)

  area = ( 5 * s * s ) / ( 4 * math.tan(math.pi/5) )

  print("The area of the pentagon is", format(area, ".2f") )

if __name__ == "__main__":
    main()