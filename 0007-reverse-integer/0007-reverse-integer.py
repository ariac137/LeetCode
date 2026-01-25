class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(x)
        result = ""
        if (str_x[0] == "-"):
            result = result + str_x[0]
            str_x = str_x[1:]
        for i in str_x[::-1]:
            result = result + i
        print(result)
        val = int(result)
        if -2**31 <= val <= 2**31 - 1:
            return val
        return 0