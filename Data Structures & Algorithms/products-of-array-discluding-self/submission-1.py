class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res, prod = [0] * len(nums), 1
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if j != i:
                    prod *= nums[j]
            res[i] = prod
        return res