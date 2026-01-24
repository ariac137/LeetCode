class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevNum = {}
        for i in range(len(nums)) :
            diff = target - nums[i]
            if diff in prevNum:
                return [prevNum[diff], i]
            prevNum[nums[i]] = i
