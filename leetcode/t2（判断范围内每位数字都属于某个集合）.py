#输入两个数A，B，显示A~B范围内，所有位上的数字都属于
# 集合{1，3，4，8，9}的数字，如果A>B，则交换A，B

def search(A,B):

    if A>B:
        C=A
        A=B
        B=C
    #如果A大于B，则交换

    num=['1','3','4','8','9']


    for i in range(A,B) :
        count = 0
        for c in str(i) :
            if c in num :
                count += 1
                #count用来计数，当遍历完每一个数字的时候，确定每位数字都在集合中
            if count == len(str(i)):
                print(i)


if __name__=="__main__":
    search(120,11)