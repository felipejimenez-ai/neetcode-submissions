from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        I think that we could iterate the array and put each new number into a set.
        Then if a number is already in the set, we return True.

        Empty array -> False
        All elements same -> True

        [PSEUDOCODE]

        Create an empty set (let’s call it seen).

        Iterate through each number in the array:

            - If the number is already in seen, return True (found a duplicate).

            - Otherwise, add the number to seen.

        If you finish the loop without finding a duplicate, return False.
        """
        
        seen = set()

        for num in nums:
            if num in seen: return True
            else: seen.add(num)
        
        return False