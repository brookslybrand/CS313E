#Write a program that reads the following information
#and prints a payroll statement:
#  Employee’s name (e.g., Smith)
#  Number of hours worked in a week (e.g., 10)
#  Hourly pay rate (e.g., 9.75)
#  Federal tax withholding rate (e.g., 20%)
#  State tax withholding rate (e.g., 9%)


import math

def dollarFormat (n):
  return format(n, ".3f")[:-2]#.strip("0")

def main():


  # read in informatio    
  name = str(input("Enter employee's name: "))

  hrs = float(input("Enter number of hours worked in a week: "))

  p_rate = float(input("Enter hourly pay rate: "))

  p_gross = hrs * p_rate;

  f_tax = float(input("Enter federal tax withholding rate: "))

  s_tax = float(input("Enter state tax withholding rate: "))

  f_wh = p_gross * f_tax

  s_wh = p_gross * s_tax

  deductions = f_wh + s_wh

  #print information
  #print("\nEmployee Name:", name )

  print("Hours Worked:", hrs )

  print("Pay Rate: $", dollarFormat(p_rate) )

  print("Gross Pay: $", dollarFormat(p_gross) )

  print("Deductions:")

  print(" Federal Witholding $"
      , dollarFormat(f_wh)
     )

  print(" State Witholding $"
      , dollarFormat(s_wh)
     )

  print(" Total Deduction $"
      , dollarFormat(deductions)
     )

  print("Net Pay: $"
      , dollarFormat(p_gross - deductions)
     )

if __name__ == "__main__":
  main()