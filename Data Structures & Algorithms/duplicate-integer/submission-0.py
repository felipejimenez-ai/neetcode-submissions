class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = 0
        counter_dict = {}
        # iterate
        for i in nums:
            # count
            if counter_dict.get(i) == None:
                counter_dict[i] = 1
            else:
                return True
        return False