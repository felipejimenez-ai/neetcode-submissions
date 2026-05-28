class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        sub = ""
        lonSub = 0

        while r < len(s):
            if s[r] in sub: 
                sub = ""
                l += 1
                r = l
            
            sub += s[r]
            print(sub)
            lonSub = max(lonSub, len(sub))
            r += 1

        return lonSub