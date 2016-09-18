
# give the value of a certain sum to a certain number of additions

def my_sum(last_num):
    '''builds an alternating sequence
    '''
    sequence = lambda n: ( 2*n - 1 )/( 2*n + 1 )
    series = sum(sequence(n) for n in range(1, ( (97 + 1) // 2) + 1))
    return series
  

def main():

  print( my_sum(97) )
    
if __name__ == "__main__":
  main()


# In[ ]:



