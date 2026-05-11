class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency = {}
        for n in nums:
            if n not in frequency:
                frequency[n] = 0
            frequency[n] += 1
        return max(frequency, key=frequency.get)