# calculate the area of a regular polygon given the number of size
import math

def main():
  n = int(input("Enter the number of sides: "))

  s = float(input("Enter the side: "))

  area = ( n * math.pow( s, 2 ) ) / ( 4 * math.tan( math.pi/n ) )

  print("The area of the polygon is", area )

if __name__ == "__main__":
    main()