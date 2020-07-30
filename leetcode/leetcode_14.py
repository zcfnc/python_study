# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 :
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
#考虑问题：
#1.只有一个元素返回自身
#2.列表为空返回空字符

#思路：从下标为0开始比较每一位的字符是否相同并保存起来
def longestCommonPrefix(strs):

    if not strs:
        return ''
    # 在使用max和min的时候已经把字符串比较了一遍
    # 当前列表的字符串中，每个字符串从第一个字母往后比较直至出现ASCII码 最小的字符串
    s1 = min(strs)
    print(s1)
    # 当前列表的字符串中，每个字符串从第一个字母往后比较直至出现ASCII码 最大的字符串
    s2 = max(strs)
    print(s2)
    # 使用枚举变量s1字符串的每个字母和下标
    for i, c in enumerate(s1):
        # 比较是否相同的字符串，不相同则使用下标截取字符串
        if c != s2[i]:
            return s1[:i]
    return s1

if __name__=="__main__":
    strs=["aca","abadsdsd","dsdsda"]
    print(longestCommonPrefix(strs))
