def nextGreaterElement(findNums, nums):
    """
    :type findNums: List[int]
    :type nums: List[int]
    :rtype: List[int]
    """
    ans = []
    for i, item in enumerate(findNums):
        j = nums.index(item)
        while j < len(nums):
            temp = -1
            if nums[j] > item:
                temp = nums[j]
                break
            
            j += 1

        
        ans.append(temp)


    return ans

