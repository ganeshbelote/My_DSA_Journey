def printNTimes(name,n):
    if n <= 0:
        return
    print(name+str(n))
    printNTimes(name,n-1)

printNTimes("ganu",5)