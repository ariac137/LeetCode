class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        # print(MAX_INT, MIN_INT)
        sign = -1 if x < 0 else 1
        rev = 0
        x = abs(x)
        
        while x != 0:
            digit = x % 10
            x //= 10
            if rev > MAX_INT // 10:
                return 0
            # If rev == MAX_INT // 10, check if the digit pushes it over the edge
            if rev == MAX_INT // 10 and digit > 7:
                return 0
                
            rev = rev * 10 + digit
        
        return rev*sign

