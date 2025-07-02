def largestEle(arr):
    length = len(arr)
    for i in range(0,length):
        if i != 0:
            break
        for j in range(0,length - i - 1):
            if arr[j + 1] < arr[j]:
                arr[j + 1],arr[j] = arr[j],arr[j + 1]
    print(arr[-1])
    return arr[-1]

def largestEle2(arr):
    max = arr[0]
    length = len(arr)
    for i in range(1,length):
        if arr[i] > max:
            max = arr[i]
    print(max)
    return max


largestEle([2,-1,5,7,3,12,-34,18,-55])
largestEle2([2,-1,5,7,3,12,-34,18,-55])

