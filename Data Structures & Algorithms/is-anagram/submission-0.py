from optparse import Values


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f"""
        Iterate the strings and have a dictionary to count the characters.
        At the end compare the dictionaries and return True if are equal.

        [PSEUDOCODE]
        * Compare length of the arrays.
            * If are different, return False.
        * If length is zero, return True.
        * Create a dictionary that will increment the character count
          in the first string, and decrement in the second string.
        * If any decrement step is below zero, return False.
        """

        s_size = len(s)
        t_size = len(t)

        if s_size != t_size: return False
        elif (s_size or t_size) == 0: return True

        char_count = {}

        for c in s:
            char_count[c] = char_count.get(c, 0) + 1

        for c in t:
            char_count[c] = char_count.get(c, 0) - 1
            if char_count[c] < 0: return False

        if all(value == 0 for value in char_count.values()): return True
        else: return False