# 给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
# 如果不存在最后一个单词，请返回 0 。
# 说明：一个单词是指由字母组成，但不包含任何空格的字符串。
# 示例:
# 输入: "Hello World"
# 输出: 5

def lengthOfLastWord(s):


    ssplit = s.split(" ")

    result=[]

    if not s:   #字符串非空
        return 0

    for c in ssplit:
        if c!="":
            result.append(c)

    if result:
      return len(result[len(result) - 1])
    else:
        return 0

if __name__=="__main__":

    s=" "
    result=lengthOfLastWord(s)
    print(result)



