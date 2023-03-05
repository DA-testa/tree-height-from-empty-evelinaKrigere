# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    max_height = 0
    dzilums1 = [0] * n
    # Your code here
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
    n = int(input())
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
     input_values = input().split()
    parents = []
    for i in range(n):
        parents.append(int(input_values[i]))


    print(compute_height(n, parents))
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))