#反转整数
# 给定一个 32 位有符号整数，将整数中的数字进行反转。
#
# 示例:
#
# 输入: 123
# 输出: 321

s=-1234
slist=[]
ind=1

if str(s)[0]=='-':
    ind-=1
for c in str(s).replace("-",''):
    slist.append(c)
num=0
for i in range(0,len(slist)):
    num+=int(slist[i])*(10**i)

if ind==0:
    num=-num
print(num)
