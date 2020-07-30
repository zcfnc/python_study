# 动态规划
# 注意init中变量的定义与使用

class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        #self.nums定义方法中的全局变量
        self.count = [0] * len(nums)
        #count[i]表示前i个元素的和，如要求i到j之间的和，即为count[j]-count[i-1]
        for i in range(0, len(nums)):
            if i == 0:
                self.count[i] = nums[i]
            else:
                self.count[i] = nums[i] + self.count[i - 1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == j:
            return self.nums[i]
        elif i == 0:
            return self.count[j]
        else:
            return self.count[j] - self.count[i - 1]