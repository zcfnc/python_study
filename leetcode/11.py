

nums=[3,4,5,1,2]
def getMin(nums):
    l = len(nums)
    leftIndex=0
    rightIndex=l-1

    while(nums[leftIndex] > nums[rightIndex]):
        if(nums[leftIndex] > nums[rightIndex]):
            leftIndex = l // 2