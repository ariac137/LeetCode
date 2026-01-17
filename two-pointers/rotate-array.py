class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_k = k % len(nums)
        if new_k == 0:
            return
        temp_last = nums[-new_k:]
        i = len(nums) - new_k - 1
        j = len(nums) - 1
        while i >= 0:
            nums[j] = nums[i]
            i -= 1
            j -= 1
        for m in range(new_k):
            nums[m] = temp_last[m]