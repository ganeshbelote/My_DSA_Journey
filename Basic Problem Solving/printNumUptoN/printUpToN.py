def printUpToN(i,num):
    if(i > num):
        return
    print(i)
    printUpToN(i+1,num)

printUpToN(1,7)