def majorityElement(nums):

    n=len(nums)
    nums.sort()
    print(nums[int(n/2)])
    return nums[int(n/2)]




nums=[3,3,4]
majorityElement(nums)