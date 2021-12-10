import sys

def playBingo(infile):
    numbers = None
    B = []
    Results = []
    board = []
    boardwins = []

    for line in infile:
        line = line.strip()
        if numbers is None:
            numbers = [int(x) for x in line.split(',')]
        else:
            if line:
                board.append([int(x) for x in line.split()])
            else:
                if board:
                    B.append(board)
                board = []
    B.append(board)

    for b in B:
        assert len(b)==5 and len(b[0])==5
        Results.append([[False for _ in range(5)] for _ in range(5)])
    for b in B:
        boardwins.append(False)
    #print(numbers)
    #print(B)
    #print(Results)
    for num in numbers:
        for b in range(len(B)):
            #select the number
            for r in range(5):
                for c in range(5):
                    if B[b][r][c] == num:
                        Results[b][r][c] = True 
            bingo = False
            
            #check for the wins for rows
            for r in range(5):
                row_bingo = True
                for c in range(5):
                    if Results[b][r][c] == False:
                        row_bingo = False
                if row_bingo:
                    bingo = True
            #check for the wins for cols
            for c in range(5):
                col_bingo = True
                for r in range(5):
                    if Results[b][r][c] == False:
                        col_bingo = False
                if col_bingo:
                    bingo = True
            
            #if bingo, print the number
            if (bingo and not boardwins[b]):
                boardwins[b] = True
                nwin = len([j for j in range(len(B)) if boardwins[j]])
                if nwin == 1 or nwin == len(B):
                    nsum = 0
                    for r in range(5):
                        for c in range(5):
                            if Results[b][r][c] == False:
                                nsum += B[b][r][c]
                    print(nsum * num)
                
                #For the first part, just return 
                #return

                



if __name__ == '__main__':
    infile = open("input4.txt", "r")
    playBingo(infile)
    
                 




        
