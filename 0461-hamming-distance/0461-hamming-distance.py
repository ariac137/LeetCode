class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_bit = self.generateRevBits(x)
        y_bit = self.generateRevBits(y)
        print(x_bit, y_bit)
        
        count = 0
        
        extend = (abs(len(x_bit) - len(y_bit))) * "0"
        
        if len(x_bit) < len(y_bit):
            x_bit += extend
        else:
            y_bit += extend
            
        for i in range(len(x_bit)):
            if x_bit[i] != y_bit[i]:
                count += 1
            
        
        return count
        
        
        
    def generateRevBits(self, x: int) -> str:
        if x == 0:
            return "0"
        
        if x == 1:
            return "1"
        
        result = ""
        
        while x != 1:
            bit = x % 2
            result = result + str(bit)
            x = x // 2
            
        return result + "1"