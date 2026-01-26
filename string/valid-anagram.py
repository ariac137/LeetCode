class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        SIZE = 26
        count = [0 for _ in range(SIZE)]
        for char in s:
            index = ord(char) - ord('a')
            count[index] += 1
            
        for char in t:
            index = ord(char) - ord('a')
            count[index] -= 1
            if count[index] < 0:
                return False
        
        return not any(count)