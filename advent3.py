import functools

def powerconsumption(Lines,length):

    total = len(Lines)
    code = [0] * length
    gamma = 0
    epsilon = 0 
    for lines in Lines:
        for i in range(0,length):
            if lines[i] == '1':
                code[i] = code[i]+1

    for i in range(0,length):
        if code[i] >= total * 0.5:
            gamma += pow(2,(length-1) - i)
            code[i] = 1
        else:
            epsilon += pow(2,(length-1) - i)
            code[i] = 0
    return epsilon , gamma, code

def calculateoxy(Lines,length,code):
    k = 0
    while len(Lines) > 1:
        Lines = list(filter(lambda x:int(x[k])==code[k], Lines))
        _, _, code = powerconsumption(Lines,length)
        k+=1
    return Lines

def calculatescuba(Lines,length,code):
    k = 0
    while len(Lines) > 1:
        Lines = list(filter(lambda x:int(x[k])==1-code[k], Lines))
        _, _, code = powerconsumption(Lines,length)
        k+=1
    return Lines

if __name__ == '__main__':
    file1 = open("input3.txt", "r")
    Lines = file1.readlines()
    length = len(Lines[0]) -1 #there is one empty character at the end of input
    epsilon, gamma, code = powerconsumption(Lines,length)
    oxy = calculateoxy(Lines,length,code)
    scuba = calculatescuba(Lines,length,code)
    
    print(epsilon * gamma)
    print(int(oxy[0], 2) * int(scuba[0], 2))

#Optiized solution

input_file = open('input3.txt').read().split()

sums = functools.reduce(lambda a,b: {k:a[k]+b[k] for k in range(12)},map(lambda x:{k:int(x[k]) for k in range(12)}, input_file))

n1 = ['1' if sums[k]>500 else '0' for k in range(12)]
n2 = ['0' if sums[k]>500 else '1' for k in range(12)]
int(''.join(n1),2)*int(''.join(n2),2)
