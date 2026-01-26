class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        count = [0] * 26  # Shorthand for initialization
        ord_a = ord('a')  # Cache this value so you don't call it in the loop
        
        for char in s:
            count[ord(char) - ord_a] += 1
            
        for char in t:
            idx = ord(char) - ord_a
            count[idx] -= 1
            if count[idx] < 0:
                return False
        
        return True # No need for any() if lengths were equal!