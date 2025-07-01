def maxMinFreq(arr):
    hash = {}
    for i in arr:
        if i not in hash:
            hash[i] = 1
        else:
            hash[i] += 1
    maxFreq = -1
    minFreq = float('inf')
    max = 0
    min = 0
    for key,val in hash.items():
        if val > maxFreq:
            max = key
            maxFreq = val
        if val < minFreq:
            min = key
            minFreq = val

    print({"Max":max,"Min":min})
    return {"Max":max,"Min":min}

maxMinFreq([1,1,2,3,3,4,4,4])
