class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
            # print(freq)
        
        for key, num in freq.items():
            if num == 1:
                return key