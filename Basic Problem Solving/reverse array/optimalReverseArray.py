def reverse(arr):
    arr.sort()
    start = 0
    end = len(arr) - 1

    while start < end :
        if arr[start] > arr[end]:
            arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1
    print(arr)
    return arr

reverse([1,2,7,3,-5])