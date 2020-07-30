# 将2的幂写成二进制很容易看出，2的幂的二进制只有一个1，其余全是0，如下所示：
# 000010000...00
# 而将2的幂的二进制减1，其二进制变为：
# 000001111...11
# 所以判断一个数是不是2的幂的方法为使用按位与操作，如果结果为0，则是2的幂：
# n & (n-1)

class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n < 0:
            return False

        s = bin(n)
        if s.count("1") == 1:
            return True
        else:
            return False