# python3

import sys
import threading
import numpy

def compute_height(n, parents):
    # Write this function
    augstums = {i: 0 for i in range(n)}
    max_height=0

    # Your code her
    rinda = []

    for i, parent in enumerate(parents):
        if parent == -1:
            rinda.append(i)

    while rinda:
        elements = rinda.pop(0)
        augstums1 = augstums[elements]

        for i, parent in enumerate(parents):
            if parent == elements:
                augstums[i] = augstums1 + 1
                rinda.append(i)
                
    max_height = max(augstums.values())
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

        parents=input()
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
