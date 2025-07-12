var rotate = function(nums, k) {
    for(let i= 0; i < k;i++){
        nums.unshift(nums.pop())
    }
    return nums
};

var optimalRotate = (nums, k) => {
    // let res
    // let end = nums.length
    // let rotatedPart = nums.splice(end - k,k)
    // res = [...rotatedPart,...nums]
    // console.log(res)
    // return res
    let end = nums.length
    let rotatedPart = nums.splice(end - k,k)
    let remainedPart = nums
    nums = [...rotatedPart,...remainedPart]
    console.log(nums)
    return nums
}

optimalRotate([-1,-100,3,99],2)
optimalRotate([1,2,3,4,5,6,7],3)
