
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 你可以假设数组中无重复元素。
# 示例 1:
# 输入: [1,3,5,6], 5
# 输出: 2

def searchInsert(nums, target):

    for n in nums:
        if n>=target:
            return nums.index(n)
    return nums.index(n) + 1


if __name__=="__main__":

    nums=[1,3,5,6]
    target=5
    print(searchInsert(nums, target))