# give the number of days for a given month and year

def main():
  
  # inputs
  m = int(input("Enter Month: "))
  y = int(input("Enter Year: "))
    
  # months
  monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']  
  monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                
  # function that handles leap year exceptions
  def leap(month):
    if (month == 'February' and y % 4 == 0):
      return 29
    else:
      return monthDays[m - 1]

  # output
  month = monthNames[m - 1]
  print( month, y, "has", leap(month) , "days")

    
if __name__ == "__main__":
  main()

