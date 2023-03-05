# python3

import sys
import threading
import numpy

def compute_height(n, parents):
    # Write this function
    dzilums1 = [0] * n
    max_height=0
    
    # Your code her
    for i in range(n):
        dzilums = 0
        elements = i
        while elements != -1:
            dzilums += 1
            elements = parents[elements]
        elements1 = i
        while elements1 != -1:
            dzilums1[elements1] = dzilums
            dzilums -= 1
            elements1 = parents[elements1]
    max_height = max(dzilums1)
    return max_height

def main():
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    n = input()

    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result

    if "I" in n:
        n=int(input())

        parents=inpu()
        parents=parents.split()
        parents=map(int,parents)
        parents=list(parents)

        print(compute_height(n,parents))



    


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
