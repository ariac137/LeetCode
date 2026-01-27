class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        prev = None
        i = 0
        j = 0
        while i < n:
            if (nums[i] != prev):
                nums[j] = nums[i]
                prev = nums[j]
                j += 1
                i += 1
            else:
                i += 1
        return j
            
                
        