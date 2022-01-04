import numpy as np

def expandMin(terrainmap,minloc):
    visited =[]
    to_visit = [minloc]
    while len(to_visit)>0:
        to_expand = to_visit.pop()
        if to_expand not in visited:
            visited.append(to_expand)
            to_try = [(to_expand[0]+1,to_expand[1]), 
                      (to_expand[0]-1,to_expand[1]), 
                      (to_expand[0],to_expand[1]+1), 
                      (to_expand[0],to_expand[1]-1)]
            for possible_next in to_try:
                if possible_next not in visited:
                    if terrainmap[possible_next[0], possible_next[1]] < 9:
                        to_visit.append(possible_next)
    return len(visited)



def findMin(terrainmap):
    mins = []
    minlocs = []
    for i in range(1,101):
        for j in range(1,101):
            if terrainmap[i,j] < terrainmap[i,j+1] and \
                terrainmap[i,j] < terrainmap[i,j-1] and \
                terrainmap[i,j] < terrainmap[i+1,j] and \
                terrainmap[i,j] < terrainmap[i-1,j]:
                    mins.append(terrainmap[i,j])
                    minlocs.append((i,j))
    print(sum(mins)+len(mins))
    sizes = np.ones(len(mins))
    for i in range(3,len(mins)):
        print(terrainmap)
        print(minlocs[i])
        sizes[i] = expandMin(terrainmap, minlocs[i])
    sizes = sorted(sizes)
    print(sizes[-1]*sizes[-2]*sizes[-3])

if __name__ == '__main__':
    file1 = open("input9.txt", "r")
    hundreds = file1.read().split()
    #save input 100x100 to a matrix 
    terrainmap = np.zeros((100,100))
    for i in range(100):
        for j in range(100):
            c = hundreds[i][j]
            terrainmap[i,j] = int(c)
    print(terrainmap.shape)
    
    a = np.ones(100)*9
    terrainmap = np.c_[terrainmap,a]
    terrainmap = np.c_[a,terrainmap]
    print(terrainmap.shape)
    b = np.ones(102)*9
    b = b.reshape(1,-1)
    terrainmap = np.r_[terrainmap,b]
    terrainmap = np.r_[b,terrainmap]
    findMin(terrainmap)
        