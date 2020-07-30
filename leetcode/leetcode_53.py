
#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 示例:
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。


def maxSubArray(nums):
    result=0
    for i in range(0,len(nums)):

        for j in range(len(nums)-1):
            addall = 0
            for c in nums[i:j]:
                addall+=c
            if result<addall:
                result=addall

    return result

if __name__=="__main__":
    nums=[1,-2,3,4,5]
    result=maxSubArray(nums)
    print(result)