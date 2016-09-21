#!/usr/bin/evn python3

from math import floor
def less_than():
    ''' Computes n**3 < 12000 '''
    return floor(12000**(1.0/3.0))

def main():
    n = 1
    while(n**3 < 12000):
        n += 1

    print(n - 1)

if __name__ == "__main__":
    main()
