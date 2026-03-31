class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        window = 0
        for num in nums:
            window += num
            maxSum = max(maxSum, window)
            if (window < 0):
                window = 0
            
        return maxSum