# python中递归需要加return 而不是直接递归
# 如第10，13，15的return

def isUgly(num):
    if num==1 or num==2|-2 :
        return 1
    if num%7==0:
        return 0
    elif num%2==0:
        print(num)
        return isUgly(num/2)
    elif num%3==0:
        return isUgly(num/3)
    elif num%5==0:
        return isUgly(num/5)
    else:
        return 0

if __name__=="__main__":
    s=isUgly(-2147483648)
    print(s)