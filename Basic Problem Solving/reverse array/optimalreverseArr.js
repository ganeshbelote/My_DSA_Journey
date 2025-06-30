function reverse(arr){
    arr.sort((a,b)=> a - b)
    let start = 0
    let end = arr.length - 1

    while(start < end){
        if(arr[start] > arr[end]){
            [arr[start],arr[end]] = [arr[end],arr[start]]
        }
        start++
        end--
    }

    console.log(arr)
    return arr
}

reverse([2,5,3,-7,1,-37,55])