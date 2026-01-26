class Solution:
    def myAtoi(self, s: str) -> int:
        # 2147483647
        MAX_INT = 2**31 - 1
        MIN_INT = - 2**31
        
        result = 0
        i = 0
        s = s.lstrip()
        sign = 1
        
        if len(s) == 0:
            return 0
        
        while i < len(s):
            if not s[i].isdigit():
                if i == 0 and s[i] == "-":
                    sign = -1
                    continue
                else:
                    break
            
            # is digit
            digit = int(s[i])
            # print(result)
            if sign*result > MAX_INT/10 or (sign*result == MAX_INT/10 and digit > 7):
                return MAX_INT
                
            if sign*result < MIN_INT/10 or (sign*result == MAX_INT/10 and digit > 8):
                return MIN_INT
            
            result = result * 10 + digit
            i += 1
        
        return sign*result
            

            
            
            
            
            