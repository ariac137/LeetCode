class Solution:
    def reverse(self, x: int) -> int:
        # Step 1: Handle the sign
        s = (x > 0) - (x < 0)  # Returns 1 for positive, -1 for negative, 0 for zero
        
        # Step 2: Convert abs(x) to string, reverse it with slicing [::-1], and convert back
        # Slicing is implemented in C and is incredibly fast
        res = int(str(abs(x))[::-1]) * s
        
        # Step 3: Fast bit-wise range check
        # 2**31 is 2147483648. We check if res fits in 32-bit signed range.
        if res < -2147483648 or res > 2147483647:
            return 0
            
        return res