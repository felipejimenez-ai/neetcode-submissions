class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = {}
        lon_sub = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1

            if (r - l + 1) - max(freq.values()) > k:
                freq[s[l]] = freq.get(s[l], 0) - 1
                l += 1

            lon_sub = max(lon_sub, r - l + 1)
            # print(freq, lon_sub)

        return lon_sub