
import numpy as np
import collections

def calculateDiagram(infile):
    print(len(infile))
    covered = []
    for line in infile:
        line = line.split(" -> ")
        x1 = int(line[0].split(",")[0])
        y1 = int(line[0].split(",")[1])

        x2 = int(line[1].split(",")[0])
        y2 = int(line[1].split(",")[1])



        if(x1 == x2):
            if y2 > y1:
                for i in range(y1,y2+1):
                    covered.append((x1,i))
            else:
                for i in range(y2,y1+1):
                    covered.append((x1,i))
        elif(y1 == y2):
            if x2 > x1:
                for i in range(x1,x2+1):
                    covered.append((i,y1))
            else:
                for i in range(x2,x1+1):
                    covered.append((i,y1))
        elif(abs(x1 - x2) == abs(y1-y2)):
            sx = (x2 - x1) / abs(x2 - x1)
            sy = (y2 - y1) / abs(y2 - y1)
            for i in range(abs(x2-x1)+1):
                covered.append((x1+i*sx,y1+i*sy))
    c =collections.Counter(covered)
    count = 0
    # Just output counts > 1
    for k, v in c.items():
        if v >= 2:
            count+=1
    print(count)


if __name__ == '__main__':
    infile = open("input5.txt", "r").readlines()
    calculateDiagram(infile)