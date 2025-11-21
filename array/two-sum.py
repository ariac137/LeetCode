class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed_list = list(enumerate(nums))
        indexed_list.sort(key=lambda item: item[1])
        sorted_values = [item[1] for item in indexed_list]
        original_indices_after_sort = [item[0] for item in indexed_list]
        i = 0
        j = len(nums) - 1
        while i < j:
            temp = sorted_values[i] + sorted_values[j]
            if temp > target:
                j -= 1
            elif temp < target:
                i += 1
            else:
                return [original_indices_after_sort[i], original_indices_after_sort[j]]
            
