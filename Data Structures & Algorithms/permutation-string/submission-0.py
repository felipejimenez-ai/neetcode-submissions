class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        d1 = {ord('a') + i: 0 for i in range(26)}
        d2 = {ord('a') + i: 0 for i in range(26)}

        # 1st slicing window
        for i in range(len(s1)):
            d1[ord(s1[i])] += 1
            d2[ord(s2[i])] += 1

        if d1 == d2:
            return True

        # next slicing window
        for i in range(len(s1), len(s2)):
            # add entering chr
            d2[ord(s2[i])] += 1
            # remove leaving chr
            d2[ord(s2[i - len(s1)])] -= 1
            # check
            if d1 == d2:
                return True

        return False
        