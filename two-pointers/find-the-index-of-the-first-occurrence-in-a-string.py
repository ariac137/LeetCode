class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            rest = len(haystack) - i
            if rest < len(needle):
                return -1
            
            if haystack[i] == needle[0]:
                if haystack[i:i+len(needle)] == needle:
                    return i
        
        return -1