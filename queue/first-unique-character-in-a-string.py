class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Step 1: Build a frequency map
        # Using a dictionary is much faster than list lookups
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        # Step 2: Find the first char with count 1
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
                
        return -1