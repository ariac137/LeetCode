class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        
        while left < right:
            mid = left + (right - left) // 2
            
            if isBadVersion(mid):
                # If mid is bad, the first bad version could be mid OR to the left.
                # So we contract the right boundary to mid.
                right = mid
            else:
                # If mid is good, the first bad version MUST be to the right.
                # So we move left past mid.
                left = mid + 1
                
        # When left == right, we have found the answer
        return left