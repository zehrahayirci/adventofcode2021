
def findLocation(Lines):

    x = 0
    y = 0 
    aim = 0

    for lines in Lines:
        word = lines.split(" ")[0]
        distance = int(lines.split(" ")[1])
        if word == "forward":
            x += distance
            y += distance * aim
        elif word == "up":
            aim -= distance
        else:
            aim += distance
    return x,y
        

if __name__ == '__main__':
	file1 = open("input2.txt", "r")
	Lines = file1.readlines() 
	x, y =findLocation(Lines)
	print(x * y)