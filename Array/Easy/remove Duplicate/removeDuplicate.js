const removeDup = arr => {
    let index = 1
    let dupIndex = 0
    
    while(index < arr.length){
        if(arr[dupIndex] != arr[index]){
            dupIndex++
            arr[dupIndex] = arr[index]
        }
        index++
    }
    console.log(dupIndex + 1)
    return (dupIndex + 1)
}

removeDup([1,2,2,3,3,4,4])