class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = ""
        for item in nums:
        	s += str(item)

        ans = 0
        for ones in s.split('0'):
        	if len(ones) > ans:
        		ans = len(ones)

        return ans

if __name__ == "__main__":
	s = Solution()
	test = [1,1,0,1]
	ans = s.findMaxConsecutiveOnes(test)
	print(ans)