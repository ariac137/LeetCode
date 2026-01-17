class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort() # Sorts in-place, O(n log n) time
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False