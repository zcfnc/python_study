#寻找一个和数的两个加数

def twoSum(nums, target):
    ind = []

    for i in range(0, len(nums) - 1):
        print(nums[i])


        for j in range(i + 1, len(nums)):
            print(nums[j])
            if nums[i] + nums[j] == target:
                ind.append(i)
                ind.append(j)
                break
    print(ind)
    return ind


if __name__ == "__main__":

    nums = [3, 2, 4]

    twoSum(nums,6)