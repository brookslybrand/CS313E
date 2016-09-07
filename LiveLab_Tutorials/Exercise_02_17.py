# Compute BMI

def main():

  # prompt for weight in lbs
  weight_lbs = float(input("Enter weight in pounds: "))
  height_in = float(input("Enter height in inches: "))

  # convert weight and height
  weight_kg = weight_lbs*0.45359273
  height_m = height_in*0.0254
    
  # calculate BMI
  bmi = weight_kg/(height_m**2)

  # print result
  print("BMI is", bmi)


if __name__ == '__main__':
    main()