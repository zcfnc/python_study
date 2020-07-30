# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# 说明：
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
# 示例 1:
# 输入: [2,2,1]
# 输出: 1
# 示例 2:
# 输入: [4,1,2,1,2]
# 输出: 4

#思想：遍历数组对每一个元素进行异或操作，异或相同为0，不同为1.则每一个都异或完
#之后就为只有一次的数字了

def singleNumber(nums):
    ss = 0
    for i in nums:
        ss = ss ^ i
    return ss

if __name__=="__main__":
    nums=[1,2,1]
    print(singleNumber(nums))