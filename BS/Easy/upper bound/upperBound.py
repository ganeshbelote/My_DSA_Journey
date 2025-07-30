def upperBound(arr,x):
    start = 0
    end = len(arr) - 1
    ans = len(arr)

    while start <= end :
        mid = (start + end) // 2
        if arr[mid] > x:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    print(ans)
    return ans 

upperBound([1,2,2,3],2)