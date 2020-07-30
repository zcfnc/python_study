# 4的幂首先是2的幂，因为4^n = (2^2)^n，所以4的幂的二进制同样只有一个1，
# 与2的幂不同的是，4的幂的二进制的1在偶数位上，所以判断一个数是不是4的幂的方式为：
# 1）首先判断是不是2的幂，使用 n & (n-1)
# 2）进一步判断与0x55555555的按位与结果，
# 0x55555555是用十六进制表示的数，其奇数位上全是1，偶数位上全是0，判断 n & 0x55555555
class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num <= 0:
            return False
        if num == 2:
            return False
        else:
            n = bin(num).split('0b')[1]
            n = n[::-1]
            if n.count("1") == 1 and list(n).index("1") % 2 == 0:
                return True
        return False