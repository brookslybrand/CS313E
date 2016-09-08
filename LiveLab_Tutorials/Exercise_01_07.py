'''
sequence outputs a single number.
enumerate behaves like the MMa MapIndexed and outputs [idx, value].
(-1)**(n%2) handles the alternating behaviour
'''
def pi_approx(denom):
    '''builds an alternating sequence and returns
    approximation of pi.
    '''
    sequence = lambda n,x: (1/x) * (-1)**(n%2)
    series = sum(sequence(n,x) for n,x in enumerate(range(1, denom+1, 2)))
    return 4 * series

#for value in [11,15]:
#  print(pi_approx(value))




def main():
  pi1 = 4 * ( 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 )
  pi2 = 4 * ( 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + 1/13 - 1/15 )
  print(pi1)
  print(pi2)


if __name__ == '__main__':
    main()
