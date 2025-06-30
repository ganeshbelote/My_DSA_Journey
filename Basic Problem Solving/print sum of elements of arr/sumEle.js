function sum(arr){
    if(!arr.length) return 0 // if(!arr) return 0 here !arr is invalid as [] is truthy in Javascript
    return arr.pop() + sum(arr) // as we are poping last element so no need of arr.slice(end - 1)
}

console.log(sum([1,2,3,4]))