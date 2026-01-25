class Solution:
    def reverse(self, x: int) -> int:
        # Convert to string, reverse, and handle the negative sign in one go
        s = str(x)
        if s[0] == '-':
            res = int('-' + s[1:][::-1])
        else:
            res = int(s[::-1])
        
        # Fast bitwise-style range check
        # Using the actual hex or decimal limit is faster than 2**31
        if res > 2147483647 or res < -2147483648:
            return 0
            
        return res