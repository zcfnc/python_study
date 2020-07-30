# 给定一个整数，写一个函数来判断它是否是 3 的幂次方。
# 示例 1:
# 输入: 27
# 输出: true
# 示例 2:
# 输入: 0
# 输出: false
# 示例 3:
# 输入: 9
# 输出: true

#思路：temp=以n为底3的对数  如果3的temp次方==n则为3的对数  同理可用到2的幂和4的幂上
import math
class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n == 1:
            return True
        if n <= 0:
            return False
        if 3 ** round(math.log(n, 3), 3) == n:
            return True
        else:
            return False
