from __future__ import print_function

import numpy as np




if __name__ == '__main__':
    file1 = open("input20.txt", "r")
    decoder = file1.readline()
    a = file1.readline()
    chunk = file1.read().split()

    dsize = 100 

    octopuses = np.zeros((dsize,dsize))

    for i in range(dsize):
        for j in range(dsize):
            c = chunk[i][j]
            if c == ".":
                octopuses[i,j] = 0
            elif c == "#":
                octopuses[i,j] = 1
    
    print(len(chunk),len(chunk[0]))
    for h in range(dsize):
        for t in range(dsize):
            c = octopuses[h,t]
            if c == 1:
                print("#", end='')

            elif c == 0:
                print(".", end='')
        print("")
    

    a = np.zeros((dsize,100))
    octopuses = np.c_[octopuses,a]
    #print(octopuses)
    octopuses = np.c_[a,octopuses]
    b = np.zeros((100,dsize+200))
    octopuses = np.r_[octopuses,b]
    octopuses = np.r_[b,octopuses]
    print("_____---------________________----")
    for h in range(dsize+200):
        for t in range(dsize+200):
            c = octopuses[h,t]
            if c == 1:
                print("#", end='')
            elif c == 0:
                print(".", end='')
        print("")
    print("_____---------________________----")
    for t in range(50):
        if t%2 == 0:
            new_octopuses = np.ones((dsize+200,dsize+200))
        else:
            new_octopuses = np.zeros((dsize+200,dsize+200))
        for i in range(1,dsize+199):
            for j in range(1,dsize+199):
                kernel = octopuses[i-1:i+2,:][:,j-1:j+2].reshape(9)
                kernel = kernel.dot(1 << np.arange(kernel.shape[-1] - 1, -1, -1))
                c= decoder[int(kernel)]
                if c == ".":
                    new_octopuses[i,j] = 0
                elif c == "#":
                    new_octopuses[i,j] = 1
        """
        for h in range(dsize+200):
            for t in range(dsize+200):
                c = new_octopuses[h,t]
                if c == 1:
                    print("#", end='')

                elif c == 0:
                    print(".", end='')
            print("")
        """

        print(new_octopuses)
        octopuses = new_octopuses
    print(np.sum(octopuses))

import matplotlib.pyplot as plt
import matplotlib.cm as cm
plt.imsave('oct.png', octopuses, cmap=cm.gray)
