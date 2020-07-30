# 给定两个二进制字符串，返回他们的和（用二进制表示）。
# 输入为非空字符串且只包含数字 1 和 0。
# 示例 1:
# 输入: a = "11", b = "1"
# 输出: "100"
# 示例 2:
# 输入: a = "1010", b = "1011"
# 输出: "10101"


def addBinary(a, b):


    al=int(a,base=2)
    bl=int(b,base=2)

    cl=al+bl
    cl=str(bin(cl)).replace("0b","")

    print(cl)



if __name__=="__main__":

    a = "11"
    b = "1"

    addBinary(a,b)