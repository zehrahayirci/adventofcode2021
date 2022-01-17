grid = set()


def fold_from_y(y):
    global grid
    line_cut = ([n for n in grid if n[1] >= y])
    for item in line_cut:
        grid.add( (item[0],y - (item[1]-y)) )
    for item in line_cut:
        grid.discard(item )

def fold_from_x(x):
    global grid
    line_cut = ([n for n in grid if n[0] >= x])
    for item in line_cut:
        grid.add( (x - (item[0]-x),item[1]) )
    for item in line_cut:
        grid.discard(item )



def fold_from(x,y):
    if x == 0:
        fold_from_y(y)
    else:
        fold_from_x(x)






if __name__ == "__main__":
    
    file1 = open("input13.txt", "r")
    lines = file1.read().split()
    for line in lines:
        x = int(line.split(",")[0])
        y = int(line.split(",")[1])
        grid.add((x,y))

    fold_from(655,0)
    fold_from(0,447)
    fold_from(327,0)
    fold_from(0,223)
    fold_from(163,0)
    fold_from(0,111)
    fold_from(81,0)
    fold_from(0,55)
    fold_from(40,0)
    fold_from(0,27)
    fold_from(0,13)
    fold_from(0,6)
    print(len(grid))
