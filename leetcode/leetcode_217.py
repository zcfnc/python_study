def containsDuplicate(nums):
    count = {}

    for n in nums:
        if n not in count:
            count[n] = 1
        else:
            count[n]+=1
        if count[n] > 1:
            return True
    print(count)
    return False
nums=[1,2,3,1]
t=containsDuplicate(nums)
print(t)