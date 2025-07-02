def isArraySorted(arr):
    for i in range(1,len(arr)):
        if arr[i - 1] > arr[i]:
            return False
    return True


print(
  isArraySorted([1, 2, 3, 4]),
  isArraySorted([1, 2, 5, 4]),
  isArraySorted([1, 2, 3, 5, 4]),
  isArraySorted([11, 2, 3, 4, 5])
)
