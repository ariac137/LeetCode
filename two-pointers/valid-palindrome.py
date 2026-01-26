class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Filter in one pass
        filtered = "".join(char.lower() for char in s if char.isalnum())
        # Compare to reverse
        return filtered == filtered[::-1]