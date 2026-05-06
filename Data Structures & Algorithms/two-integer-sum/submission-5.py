class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        saved_idx = {}
        for i, n in enumerate(nums):
            num = target - n
            if num in saved_idx:
                return [saved_idx[num], i] 
            saved_idx[n] = i
        return