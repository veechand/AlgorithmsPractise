class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        # approach: use dynamic programming approach to verify

        n = len(s)
        dp = [True] + [False] * n
        print dp
        for i in range(1, n+1):
            print "i=",i,
            for j in range(i-1, -1, -1):
                print "j=",j,
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[n]

if __name__ == "__main__":
    s = "abcdef"
    wordDict = ["abc", "def"]
    solution = Solution()
    result = solution.wordBreak(s, wordDict)
    print(result)