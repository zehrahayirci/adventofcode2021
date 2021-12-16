from scipy.optimize import minimize_scalar 
import math


carbs = []
def fun(x):
    summ = 0
    for crab in crabs:
        summ += abs(crab - x)
    return summ

def fun2(x):
    summ = 0
    for crab in crabs:
        summ += abs(crab - x) * (abs(crab - x)+1) * 0.5 
    return summ

if __name__ == '__main__':
    file1 = open("input7.txt", "r")
    crabs= file1.read().split(",")
    crabs = [int(x) for x in crabs]

    res = minimize_scalar(fun2)
    x = int(round(res.x))
    print(x)
    fuel = fun2(x)
    print(fuel)



