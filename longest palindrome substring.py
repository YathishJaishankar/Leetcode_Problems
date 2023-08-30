class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) == 1:
            return s
        N = len(s)
        memo = {}
        
        
        def dp(i,j):
            if i == j:
                return 1
            if j - i == 1:
                return s[j] == s[i]
            if (i,j) in memo:
                return memo[(i,j)]
            if s[i] == s[j]:
                ans = dp(i+1,j-1)
                memo[(i,j)] = ans
                return ans
            else:
                memo[(i,j)] = False
                #dp(i+1,j)
                #dp(i,j-1)
                return False
            
        ans = ""
        for i in range(N-1,-1,-1):
            for j in range(i,N):
                if dp(i,j) and len(s[i:j+1]) > len(ans):
                    ans = s[i:j+1]
        
        return ans