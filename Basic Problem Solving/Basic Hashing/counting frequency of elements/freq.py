def arrFreq(arr):
    hash = {}
    for i in arr:
        if i not in hash:
            hash[i] = 1
        else:
            hash[i] += 1
    return hash

print(arrFreq([1,1,2,3,4,3,4,3]))