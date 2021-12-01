def countBigger(Lines):
  
    count = 0
    before = -1
    for line in Lines:
        if int(line) > before:
            count +=1
        before= int(line)
    print(count-1)
    
def countBiggerWindow(Lines):
  
    count = 0
    before = -1
    for i in range(0,len(Lines)-2):
        midcount = int(Lines[i]) + int(Lines[i+1]) + int(Lines[i+2])
        if midcount > before:
            count +=1
        before= midcount
    print(count-1)
if __name__ == '__main__':
	file1 = open("input1.txt", "r")
	Lines = file1.readlines() 
	countBigger(Lines)
	countBiggerWindow(Lines)