
def two_sum(arr, target):
    for i in range(0,len(arr)):
        for j in range(i,len(arr)):
            if (arr[i] + arr[j]) == target:
                return [i, j]
    return []


## O(n) solution by xxfer

##def twoSum(nums, target):
##    """
##    :type nums: List[int]
##    :type target: int
##    :rtype: List[int]
##    """
##    d={}
##    for i, n in enumerate(nums):
##        if n in d:
##            return (d[n], i)
##        else:
##            d[target-n]=i
##    return (0,0)
