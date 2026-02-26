class Solution:
    def romanToInt(self, s: str) -> int:
        ROMAN_NUMS = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        
        result = 0
        for i in range(len(s) - 1):
            if ROMAN_NUMS[s[i]] >= ROMAN_NUMS[s[i + 1]]:
                result += ROMAN_NUMS[s[i]]
            else:
                result -= ROMAN_NUMS[s[i]]
            
            
        return result + ROMAN_NUMS[s[-1]]