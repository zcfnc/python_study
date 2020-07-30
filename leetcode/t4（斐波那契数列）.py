# #打印斐波那契数列
#



fibs=[0,1]
for i in range(10):
    fibs.append(fibs[-2]+fibs[-1])
print(fibs)
