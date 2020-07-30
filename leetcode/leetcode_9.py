#判断回文数

def isPalindrome(x):
    char=[]
    x=str(x)
    count=0

    for c in x:
        char.append(c)
    if len(char)==1:
        return True

    for i in range(0,int(len(char)/2)):
        if char[i]==char[len(char)-1-i]:
           count+=1
        if count==int(len(char)/2):
            print("true")
            return True
    print("false")
    return False

if __name__=="__main__":
    x=1123211
    isPalindrome(x)
