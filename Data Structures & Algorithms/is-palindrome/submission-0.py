import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_normalized = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        s_reversed = s_normalized[::-1]
        return s_normalized == s_reversed