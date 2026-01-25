class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        # print(MAX_INT, MIN_INT)
        sign = -1 if x < 0 else 1
        rev = 0
        x = abs(x)
        
        while True:
            digit = x % 10
            x = x // 10
            if x == 0:
                break
            rev = rev * 10 + digit
            # print(rev)
            if rev > MAX_INT or rev*sign < MIN_INT:
                return 0
        # print(rev)
        rev = rev * 10 + digit
        if rev > MAX_INT or rev*sign < MIN_INT:
            return 0
        
        return rev*sign

