class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        
        if len1 > len2:
            return False

        targetFreq = [0 for _ in range(26)]
        windowFreq = [0 for _ in range(26)]

        for i in range(len1):
            targetFreq[ord(s1[i]) - ord('a')] += 1
            windowFreq[ord(s2[i]) - ord('a')] += 1

        matches = 0

        for i in range(26):
            if targetFreq[i] == windowFreq[i]:
                matches += 1

        print(matches, targetFreq, windowFreq, '\n')

        if matches == 26:
            return True

        left = 0

        for right in range(len1, len2):
            windowFreq[ord(s2[left]) - ord('a')] -= 1
            if targetFreq[ord(s2[left]) - ord('a')] == windowFreq[ord(s2[left]) - ord('a')]:
                matches += 1
            # if before there was a match but now it doesn't, then we decrement a match
            elif targetFreq[ord(s2[left]) - ord('a')] == windowFreq[ord(s2[left]) - ord('a')] + 1:
                matches -= 1
            
            windowFreq[ord(s2[right]) - ord('a')] += 1
            if targetFreq[ord(s2[right]) - ord('a')] == windowFreq[ord(s2[right]) - ord('a')]:
                matches += 1
            # if before there was a match but now it doesn't, then we decrement a match
            elif targetFreq[ord(s2[right]) - ord('a')] == windowFreq[ord(s2[right]) - ord('a')] - 1:
                matches -= 1            

            print(matches, targetFreq, windowFreq, '\n')

            left += 1

            if matches == 26:
                return True

        return False