def rotate(nums,k):
    for i in range(0,k):
        nums.insert(0,nums.pop())
    print(nums)
    return nums


rotate([-1,-100,3,99],2)
rotate([1,2,3,4,5,6,7],3)