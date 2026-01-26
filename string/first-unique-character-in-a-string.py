class Solution:
    def firstUniqChar(self, s: str) -> int:
        duplicated_items = []
        for i in range(len(s)):
            item = s[i]
            if item in duplicated_items:
                continue
            if (i >= len(s) - 1) or item not in s[i + 1:]:
                return i
            
            duplicated_items.append(item)

            
        return -1
