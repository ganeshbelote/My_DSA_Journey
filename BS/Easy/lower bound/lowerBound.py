def lowerBound(arr,x):
    for ind,val in enumerate(arr):
            if val >= x:
                print(ind)
                return ind

def optimal(arr,x):
    ans = len(arr)
    start = 0
    end = len(arr) - 1

    while start <= end :
          mid = (start + end) // 2
          if arr[mid] >= x:
               ans = mid
               end = mid - 1
          else:
               start = mid + 1
    print(ans)
    return ans

optimal([3,5,8,15,19],9)