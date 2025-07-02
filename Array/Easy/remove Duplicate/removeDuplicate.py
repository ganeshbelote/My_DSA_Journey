# 1,2,2,3,3,4,4 => 

def removeDup(arr):
    hash = {}
    res = []
    for i in range(0,len(arr)):
        if arr[i] not in hash:
            hash[arr[i]] = 1
        else:
            hash[arr[i]] += 1
    for ele in hash.keys():
            res.append(int(ele))
    remLen = len(arr) - len(res)
    print((res + ['_']*remLen),len(res))
    return len(res)

def optimalRemDup(arr):
    dupIndex = 0
    index = 1
    while index < len(arr): # iterating each element

        if arr[dupIndex] != arr[index]: # checking if element is duplicate of previous one as it is SORTED array
            dupIndex += 1 # getting duplicate element index
            arr[dupIndex] = arr[index] # save unique element at that duplicate index

        index += 1 # yes/no no matter move to next
    return dupIndex + 1

removeDup([1,2,2,3,3,4,4])
print(optimalRemDup([1,2,2,3,3,4,4]))
