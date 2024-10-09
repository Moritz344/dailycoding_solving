def Insert(nums,target):
    for i in range(len(nums)):
        if target <= nums[i]:
            return i

    return len(nums)




print(Insert([1,3,5,6],5))
