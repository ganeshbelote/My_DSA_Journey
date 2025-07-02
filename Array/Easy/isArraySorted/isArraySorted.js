const isArraySorted = arr => {
    for(let i = 1 ; i < arr.length; i++){
        if(arr[i - 1] > arr[i]) return false
    }
    return true
}

console.log(
  isArraySorted([1, 2, 3, 4]),
  isArraySorted([1, 2, 5, 4]),
  isArraySorted([1, 2, 3, 5, 4]),
  isArraySorted([11, 2, 3, 4, 5])
)
