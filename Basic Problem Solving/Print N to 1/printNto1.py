def printFormN(num,i):
    if num < i:
        return
    print(num)
    printFormN(num-1,i)

printFormN(7,1)