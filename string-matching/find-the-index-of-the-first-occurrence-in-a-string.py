class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        while i < len(haystack):
            if haystack[i] == needle[0]:
                k = i + 1
                j = 1
                while k < len(haystack) and j < len(needle):
                    if haystack[k] != needle[j]:
                        break
                    k += 1
                    j += 1
                if j == len(needle):
                    return i
            i += 1
            
        return -1
                    