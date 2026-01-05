class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        prev = nums[0]
        i = 1
        j = 1
        while i < n:
            if (nums[i] != prev):
                nums[j] = nums[i]
                prev = nums[j]
                j += 1
                i += 1
            else:
                i += 1
        return j
            
                
        