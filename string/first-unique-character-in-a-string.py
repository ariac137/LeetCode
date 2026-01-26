class Solution:
    def firstUniqChar(self, s: str) -> int:
        duplicated_items = []
        for i in range(len(s)):
            item = s[i]
            if item in duplicated_items:
                continue
            if i >= len(s) - 1:
                return i
            if item in s[i + 1:]:
                duplicated_items.append(item)
            else: 
                return i
            
        return -1
