class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for n in nums_set:
            if n - 1 not in nums_set: # means it's the starting point
                current = n
                length = 0
                while current in nums_set:
                    current += 1
                    length += 1
                longest = max(longest, length)
        
        return longest