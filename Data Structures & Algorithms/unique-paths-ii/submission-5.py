class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        directions = [(0, 1), (1, 0)]
        dp = [[0] * n for _ in range(m)]
        if (obstacleGrid[0][0] == 1):
            return 0
        dp[0][0] = 1
        visited = set()
        pos = [(0, 0)]
        while pos:
            r, c = pos.pop(0)
            if (r > 0):
                dp[r][c] += dp[r - 1][c]
            if (c > 0):
                dp[r][c] += dp[r][c - 1]
            
            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                if (newR < 0 or newC < 0 or newR == m or newC == n or (newR, newC) in visited or obstacleGrid[newR][newC] == 1):
                    continue
                visited.add((newR, newC))
                pos.append((newR, newC))
        # for r in dp:
        #     print(r)
        return dp[-1][-1]