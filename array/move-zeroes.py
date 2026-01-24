class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        i = 0
        j = 0
        while i <= j and j < len(nums):
            while j < len(nums) and nums[j] == 0:
                j += 1
            if j >= len(nums):
                break
            nums[i] = nums[j]
            j += 1
            i += 1
        while i < len(nums):
            nums[i] = 0
            i += 1
        