class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return (x ^ y).bit_count()
        
        if x == 1:
            return "1"
        
        result = ""
        
        while x != 1:
            bit = x % 2
            result = result + str(bit)
            x = x // 2
            
        return result + "1"