const largestEle = arr => {
    let max = arr[0]
    let len = arr.length
    for (let i = 1; i < len; i++) {
        if(max < arr[i]){
            max = arr[i]
        }
    }
    console.log(max)
    return max
}

largestEle([2,-1,5,7,3,12,-34,18,-55])