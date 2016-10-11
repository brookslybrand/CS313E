def xor(c1, c2):
  return ( ( not(c1) and c2 ) or ( c1 and not(c2) ) )

def sum_digits(num):
  sum_num = 0
  while(num > 0):
    sum_num += num % 10
    num = num // 10
  return sum_num

def rev_number (num):
  rev_num = 0
  while(num > 0):
    rev_num = rev_num*10 + (num % 10)
    num = num // 10
  return rev_num

def is_palindromic (num):
  return (num == rev_number(num))

def is_prime (num):
  divisor = 2
  limit = int(num**0.5) + 1
  isPrime = True
    
  while(isPrime and divisor < limit):
    if (num % divisor == 0):
      isPrime = False
    divisor += 1
    
  return isPrime

def sum_divisors (num):
  sum_div = 0
  divisor = 1
  limit = num // 2
  while (divisor <= limit):
    if(num % divisor == 0):
      sum_div += divisor
    divisor += 1
  return sum_div

# num is a 4 digit number, return True if the sum
# of the first two digits is equal to the sum of the last two
# and False otherwise
def is_equal (num):
  num1 = num // 100
  num2 = num % 100
    
  return ((num1//10 + num1%10) == (num2//10 + num2%10))

# returns True if the digits are strictly increasing
def is_incr (num):
  last = num % 10
  while (num > 0):
    num = num // 10
    prev = num % 10
    if (prev > last):
      return False
    last = prev
  return True

# return True is point P is strictly inside the circle
def is_inside (x, y, rad, a, b):
  dist = ((x - a)**2 + (y - b)**2)** 0.5
  return (dist < rad)

def main():
  # four digit non-palindromic number whose cube is palindromic
  for x in range(1000, 10000):
    if( (not(is_palindromic(x)) and is_palindromic(x**3) )):
      print (x)
      break
        
  # print all twin primes less than 100
  for x in range(2, 100):
    twin = x + 2
    if (is_prime(x) and is_prime(twin)):
      print(x, twin)
    
  # print all three digit emirps
  for x in range(100, 1000):
    if (not (is_palindromic(x)) and is_prime(x)):
      if(is_prime(rev_number(x))):
        print(x)
        
if __name__ == "__main__":
  main()