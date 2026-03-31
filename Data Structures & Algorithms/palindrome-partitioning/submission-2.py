class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # the trick is to compute that a partition exists between i:j +1
        # and track that in a 2D array (DP)
        # then for every 
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = True

        for i in range(2, n + 1):
            for j in range(n - i + 1):
                dp[j][j + i - 1] = (s[j] == s[j + i - 1]) and (j + 1 > j + i - 2 or dp[j + 1][j + i - 2])
        
        def findPartitions(start: int) -> List[List[str]]:
            if (start >= n):
                return [[]]
            res = []

            for i in range(start, n):
                if (dp[start][i]):
                    nextPart = findPartitions(i + 1)
                    st = s[start:i + 1]
                    for part in nextPart:
                        res.append([st] + part)
            
            return res
        return findPartitions(0)
