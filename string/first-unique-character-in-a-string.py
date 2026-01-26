class Solution:
    def firstUniqChar(self, s: str) -> int:
        enum_s = list(enumerate(s))
        while enum_s:
            temp = enum_s.pop(0)
            temp_index, temp_s = temp
            length = len(enum_s)
            enum_s = [(i, item) for i, item in enum_s if item != temp_s]
            if len(enum_s) == length:
                return temp_index
        return -1