# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        if n == 1:
            return 1
        
        return self.firstBadVersion2(0, n)
        
    
    def firstBadVersion2(self, start:int, end:int) -> int:
        
        if start == end:
            return end
        
        middle = (start + end) // 2
        if isBadVersion(middle):
            return self.firstBadVersion2(start, middle)
        else:
            return self.firstBadVersion2(middle + 1, end)
        
        

        
        