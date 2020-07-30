


def removeDuplicates(nums):

    print(list(set(nums)))

    return len(list(set(nums)))


if __name__=="__main__":
    nums=[1,1,2]
    removeDuplicates(nums)