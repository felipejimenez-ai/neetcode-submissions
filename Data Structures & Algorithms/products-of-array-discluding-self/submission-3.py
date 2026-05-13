class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res= [0] * n
        prod = 1

        zero_count = nums.count(0)
        if zero_count > 1: return [0] * n

        for num in nums:
            if num != 0: prod *= num

        for i in range(n):
            if zero_count == 0: res[i] = prod // nums[i]
            elif nums[i] == 0: res[i] = prod

        return res