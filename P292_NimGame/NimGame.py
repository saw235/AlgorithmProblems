class Solution(object):

    memo = {}
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n%4 != 0
if __name__ == "__main__":
    s = Solution()
    test = 123123123
    ans = s.canWinNim(test)
    print(ans)	