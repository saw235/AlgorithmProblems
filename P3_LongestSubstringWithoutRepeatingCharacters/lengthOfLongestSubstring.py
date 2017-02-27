class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = 0

        i = 0
        j = 0
        memo = {}
        
        while j<n:
            #if mapped already
            if s[j] in memo:
                #get higher of the two index
                # index of last seen of current character
                i = max(memo[s[j]],i)

            ans = max(ans, j-i+ 1)

            #map the current character to an index
            memo[s[j]] = j+1
            j+= 1

        return ans

if __name__ == "__main__":
    sol = Solution()
    a = sol.lengthOfLongestSubstring("abcabcbb")
    print(a)
