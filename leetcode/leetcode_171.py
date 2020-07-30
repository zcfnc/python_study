# 给定一个Excel表格中的列名称，返回其相应的列序号。
# 例如，
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28
#     ...
# 示例 1:
# 输入: "A"
# 输出: 1
# 示例 2:
# 输入: "AB"
# 输出: 28

def titleToNumber(s):
    s = list(s)

    if len(s) == 1:
        return ord(s[0]) - 64
    else:
        print(((ord(s[0])) - 64) * 26 + (ord(s[1])) - 64)

titleToNumber("AA")