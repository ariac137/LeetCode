class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        commonPrefix = strs[0]

        for string in strs[1:]:
            commonPrefix = self.twoCommonPrefix(commonPrefix, string)
            if commonPrefix == "":
                return commonPrefix
        
        return commonPrefix
        
        
    def twoCommonPrefix(self, first_str:str, second_str:str) -> str:
        commonPrefix = ""
        for i in range(min(len(first_str), len(second_str))):
            if first_str[i] != second_str[i]:
                break
            # if first_str[i] == second_str[i]
            commonPrefix += first_str[i]
        
        return commonPrefix