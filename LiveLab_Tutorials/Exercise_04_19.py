# Compute the perimeter of a triangle

def main():
  
  # inputs
  s1, s2, s3 = input("Enter three edges: ").split(", ")

  s1 = int(s1)
  s2 = int(s2)
  s3 = int(s3)
    
  # output
  if (s1 + s2 < s3):
    print("The input is invalid")
  elif (s1 + s3 < s2):
    print("The input is invalid")
  elif (s2 + s3 < s1):
    print("The input is invalid")
  else:
    print("The perimeter is", s1 + s2 + s3)

    
if __name__ == "__main__":
  main()


# In[63]:

test = (1,2,3)


# In[61]:

test[4]


# In[ ]:



