# 假设你正在爬楼梯。需要 n 步你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 注意：给定 n 是一个正整数。
# 示例 1：
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 步 + 1 步
# 2.  2 步


def climbStairs( n):
    """
    :type n: int
    :rtype: int
    """
    a = 1
    b = 1
    for i in range(n):

        a, b = b, a + b
        print("a:",a)
        print("b:",b)


    return a

if __name__=="__main__":
    n=5
    climbStairs(n)