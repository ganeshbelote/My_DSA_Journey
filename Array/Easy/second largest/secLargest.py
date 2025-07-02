def secLargest(list):
    max = list[0]
    secMax = list[0]

    for i in range(1,len(list)):
        if list[i] > max:
            secMax = max
            max = list[i]
        elif list[i] > secMax and list[i] != max:
            secMax = list[i]
    print(secMax)
    return secMax

secLargest([2, -1, 5, 7, 3, 12, 35, -34, 18, -55])