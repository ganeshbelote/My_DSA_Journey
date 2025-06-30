def reverse(arr):
    if not arr:
        return []
    lastInd = len(arr) - 1
    return [arr[-1]] + reverse(arr[:lastInd]) # here [arr[-1]] is bcz arr[-1] is integer not list and we trying to add it with list

print(reverse([1,2,3]))