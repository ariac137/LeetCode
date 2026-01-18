class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[len(digits) - 1] != 9:
            return digits[:(len(digits) - 1)] + [digits[len(digits) - 1] + 1]
        
        # when last digit == 9
        i = len(digits) - 1
        if len(digits) == 1:
            return [int(d) for d in str(10)]
        
        return self.plusOne(digits[:(len(digits) - 1)]) + [0]

        
        
        
        
        
        
        # num = 0
        # for i in range(len(digits)):
        #     num = num * 10 + digits[i]
        # num = num + 1
        # return [int(d) for d in str(num)]