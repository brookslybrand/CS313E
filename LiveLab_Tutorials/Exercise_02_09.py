# NWS windchill formula

def main():
  t_a = float(input("Enter the temperature in Fahrenheit between -58 and 41: "))
  v = float(input("Enter the wind speed in miles per hour: "))

  if ( t_a < -58 or t_a > 41 ):
    print( "Temperature (Fahrenheit) cannot be below -58 or above 41" )
  elif (v < 2):
    print( "Windspeed must be above 2 (mph)" )
  else:
    t_wc = 35.74 + 0.6215*t_a - 35.75*( v**0.16 ) + 0.4275*t_a*(v**0.16)
    print("The wind chill index is ", t_wc)

if __name__ == '__main__':
    main()