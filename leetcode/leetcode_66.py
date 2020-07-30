# 给定一个非负整数组成的非空数组，在该数的基础上加一，返回一个新的数组。
# 最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
# 示例 1:
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
# 示例 2:
# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。


def plusOne(digits):
    num=''
    for c in digits:
        num+=str(c)
    print(num)
    num=int(num)
    num+=1
    result=[]
    for c in str(num):
        result.append(int(c))

    print(result)
    return result


if __name__=="__main__":

    digits=[1,2,4,5,6]
    plusOne(digits)