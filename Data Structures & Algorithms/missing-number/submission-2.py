class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        S = n * (n + 1) // 2
        return S - sum(nums)