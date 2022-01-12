import numpy as np


def is_valid(coor):
    if coor[0] >= 0 and coor[0]<=9 and coor[1] >= 0 and coor[1] <= 9:
        return True
    return False 

if __name__ == '__main__':
    file1 = open("input11.txt", "r")
    chunk = file1.read().split()
    
    octopuses = np.zeros((10,10))
    for i in range(10):
        for j in range(10):
            c = chunk[i][j]
            octopuses[i,j] = int(c)
    print((octopuses))
    flush_count = 0 
 
    count = 0 
    while np.any(octopuses >0):
        count +=1
        flushes= []
        recent_ones=0
        # At the beginning increase everyone +1 
        octopuses = octopuses +1
        
        #IF there is octopus above 10, flush
        #if any octopus above 10,, return:true, else:false
        while np.any(octopuses >= 10):
            r, c =np.where(octopuses >=10)
            flushes += [(r[i], c[i]) for i in range(r.shape[0])]
            for (x,y) in flushes[recent_ones:]:
                for k in [(-1,0),(1,0),(0,1),(0,-1),(-1,1),(1,1),(-1,-1),(1,-1)]:
                    komsu = (x+k[0],y+k[1])
                    if komsu not in flushes and is_valid(komsu):
                        octopuses[komsu[0],komsu[1]] +=1
            octopuses[r,c] = 0
            recent_ones = len(flushes)   
        flush_count+= np.sum(octopuses == 0)
        print(octopuses)
        #print(flush_count)
        print(count)