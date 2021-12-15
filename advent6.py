from collections import defaultdict, Counter

def step(lanterns):
    for i,val in enumerate(lanterns):
        if val == 0:
            lanterns[i] = 6
            lanterns.append(8)
        else:
            lanterns[i] -= 1
    
    return lanterns

def counting(c,n):
    X = c 
    for day in range(n):
        Y = defaultdict(int)
        for x,cnt in X.items():
            if x==0:
                Y[6] += cnt
                Y[8] += cnt
            else:
                Y[x-1] += cnt
        X = Y
    return sum(X.values())

if __name__ == '__main__':
    file1 = open("input6.txt", "r")
    lanterns= file1.read().split(",")
    lanterns = [int(x) for x in lanterns]
    c =Counter(lanterns)
    print(c)
    print(counting(c,80))
    print(counting(c,256))
