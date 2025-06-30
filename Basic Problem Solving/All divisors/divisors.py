import math
def printDivisors(num) :
    res = [1]
    for i in range(2,num+1):
        if(num%i == 0):
            res.append(i)
    return res

def optimalSol(num):
    res = []
    sqrt = int(math.sqrt(num))
    for i in range(1,sqrt+1):
        if num%i == 0:
            res.append(i)
            if i != num//i:
                res.append(num//i)
    res.sort()
    return res

print(printDivisors(36))
print(printDivisors(17))
print(optimalSol(36))
print(optimalSol(17))