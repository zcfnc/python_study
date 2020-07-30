# 一个长度为n的所有数字都在0~n-1范围内,数组中某些数字是重复的，
# 但不知道有几个数字重复了。请输出任意一个重复的数字
# 例：输入长度为7的数组{2，3，1，0，2，5，3}，那么对应输出的是重复的数字2或者3

def RepeatNum(n):
    for i in range(len(n)):
        m=n[i]
        if m==i:
            continue
        else :
            if m==n[m]:
                return n[n[i]]
            else:
                n[m],n[i]=n[i],n[m]
                print(n)




if __name__=="__main__":
    n=[2,3,1,0,2,5,3]
    result=RepeatNum(n)
    print(result)