class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        i = 0
        while (i < len(nums) and i <= r):
            # print(nums, i, l, r)
            while (l <= r and nums[l] == 0):
                l += 1
            while (r >= l and nums[r] == 2):
                r -= 1
            
            if (i < l):
                i += 1
                continue

            if (nums[i] == 0):
                nums[i], nums[l] = nums[l], nums[i]
            elif (nums[i] == 2):
                nums[i], nums[r] = nums[r], nums[i]
            else:
                i += 1
        