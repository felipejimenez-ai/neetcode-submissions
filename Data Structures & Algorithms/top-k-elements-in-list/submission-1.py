class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        bucket_sort = [[] for i in range(len(nums) + 1)]
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        for n, f in freq.items():
            bucket_sort[f].append(n)

        res = []
        for i in range(len(bucket_sort) - 1, 0, -1):
            for n in bucket_sort[i]:
                res.append(n)
            if len(res) == k:
                return res