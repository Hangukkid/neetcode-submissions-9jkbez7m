class Solution:
    def integerBreak(self, n: int) -> int:
        if (n == 2):
            return 1
        if (n == 3):
            return 2
        dp = [-1] * (n + 1)
        dp[0] = 0
        dp[1] = 0
        dp[2] = 1
        dp[3] = 2
        def breakInt(n: int) -> int:
            if (dp[n] != -1):
                return dp[n]
            
            for i in range(2, n):
                dp[n] = max(max(i, breakInt(i)) * max(n - i, breakInt(n - i)), dp[n])
            
            return dp[n]
        
        # print(dp)
        return breakInt(n)