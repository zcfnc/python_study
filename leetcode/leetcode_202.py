def isHappy(n):
    list=[]
    count=0
    for c in str(n):
        list.append(c)
    for n in list:
        count+=int(n)**2
    if count==1:
        print("ishappy")
        return True
    else:
        isHappy(count)
        return False

isHappy(20)

