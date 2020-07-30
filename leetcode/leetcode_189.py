from collections import deque


def rotate( nums, k):
    from collections import deque

    deque = deque(nums)
    deque.rotate(k)
    print(list(deque))


nums=[1,2,3,4,5,6,7]
k=3
rotate(nums,k)