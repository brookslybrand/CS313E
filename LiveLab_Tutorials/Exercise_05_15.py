
# coding: utf-8

# In[7]:

# find the larges integer n such that n**3 < 12000

def main():
  
  n = 1
  while(n**3 < 12000):
    n = n + 1

  print(n - 1)

if __name__ == "__main__":
  main()

