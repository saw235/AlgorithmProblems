class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cond_ALLCAPS = word == word.upper()
        cond_ALLLOWER = word == word.lower()
        cond_FIRSTCAPONLY = word[0] == word[0].upper() and word[1:] == word[1:].lower()

        return cond_ALLCAPS or cond_ALLLOWER or cond_FIRSTCAPONLY


if __name__ == "__main__":
    s = Solution()
    test = "FlaG"
    ans = s.detectCapitalUse(test)
    print(ans)	