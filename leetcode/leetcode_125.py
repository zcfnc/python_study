# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
# 说明：本题中，我们将空字符串定义为有效的回文串。
# 示例 1:
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 示例 2:
# 输入: "race a car"
# 输出: false


def isPalindrome(s):

    temp=[]

    for c in s:
        if c.isalnum():     #判断是否为数字或者字母
            temp.append(c)

    transtostr=str(temp).lower().replace("[","").replace("]","").replace(" ","")
    print(transtostr)
    print(transtostr[::-1])

    if transtostr==transtostr[::-1]:
        print("1")
        return True
    else:
        print("2")
        return False




if __name__=="__main__":

    s="A man, a plan, a canal: Panama"
    isPalindrome(s)