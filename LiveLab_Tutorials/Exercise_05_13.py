
# coding: utf-8

# In[86]:

# find all numbers divisible by 5 and 6, but not both

def div_test(n):
  '''
  return True if n is divisible by 5 or 6, but not both
  '''
  return ( ( ( not (n % 5) ) or ( not (n % 6) ) ) and (n % 30 != 0) )

def main():
    
  a = []
  for n in range(100, 201): # test for 100-200
    if( div_test(n) ):
      a.append(n)
    
  for i in range(1, len(a) + 1): # print answers, 10 per line
    if (i % 10):
      print (a[i-1], end=" ")
    else:
      print (a[i-1])

if __name__ == "__main__":
  main()

