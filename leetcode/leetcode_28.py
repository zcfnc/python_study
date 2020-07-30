
def strStr(haystack, needle):

    if not needle and haystack:
        return 0

    if needle in haystack:
        print(haystack.index(needle))
        return haystack.index(needle)
    else:
        print("-1")
        return -1

if __name__=="__main__":
    haystack = ""
    needle = ""
    result=strStr(haystack, needle)
    print(result)