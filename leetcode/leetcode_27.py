
def removeElement(nums, val):

    if not nums:
        return ""
    if val in nums and nums.count(val) >= 1:
        for i in range(nums.count(val)):
            nums.remove(val)

    return len(nums)

if __name__=="__main__":
    nums=[]
    val=0
    print(removeElement(nums,val))