from itertools import starmap
from traceback import print_tb


def staircase():
    n = 6
    
    for i in range(1,n+1):
        print (' '*(n-i) + "#"*i,end=' ')
        print()
    
staircase()