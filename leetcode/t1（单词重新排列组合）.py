#给出字符串abc，输出a,b,c的各种连接输出方式
#例：输入ABC，输出 ABC，ACB，BAC，BCA，CAB，CBA

def combination():

    s=input("input string!\n")
    All=[]

    for c1 in s :
        for c2 in s :
            if c1 != c2 :
                for c3 in s :
                    if c3 != c1 and c3 != c2:
                        count = c1 + c2 + c3
                        All.append(count)
    print(All)

    return All

if __name__=="__main__":
    combination()
