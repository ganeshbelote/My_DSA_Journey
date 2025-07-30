const lowerBound = (arr,x) => {
    let start = 0
    let end = arr.length - 1
    let ans = arr.length

    while( start <= end ){
        let mid = Math.floor((start + end)/2)
        if(arr[mid] >= x){
            ans = mid
            end = mid - 1
        }else{
            start = mid + 1
        }
    }
    console.log(ans)
    return ans
}

var searchInsert = function (nums, target) {
    let s = 0, e = nums.length - 1, a = 0;
    while (s <= e) {
        let m = Math.floor(s / 2 + e / 2)
        if (nums[m] == target) return m
        else if (nums[m] < target) {
            s = m + 1
        }
        else {
            e = m - 1
            a = m
        }
    }
    if (target > nums[nums.length - 1]) return nums.length
    else return a

};

console.log(searchInsert([3,5,8,15,19],9))