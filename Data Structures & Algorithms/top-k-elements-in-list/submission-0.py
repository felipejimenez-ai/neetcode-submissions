class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} # frequency of n in nums
        res = []
        for n in nums:
            if n not in freq:
                freq[n] = 1
            else: 
                freq[n] += 1
        for i in range(k):
            max_value = max(freq, key=freq.get)
            freq.pop(max_value)
            res.append(max_value)
        return res