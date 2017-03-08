class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ans = 0
        for num in nums:
        	ans ^= num

        return ans

        	
        	



        
if __name__ == "__main__":
    s = Solution()
    test = [1,1,2,2,3,4,4,5,5]
    ans = s.singleNumber(test)
    print(ans)