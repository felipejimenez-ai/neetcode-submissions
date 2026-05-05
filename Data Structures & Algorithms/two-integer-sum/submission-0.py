from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Goal: Find to numbers i and j, so i + j = target
        Input: Array of integers nums, and an integer target
        Output: Array containing the indexes -- starting with the smaller index

        One approach could be brute force. We could take one index, and do the
        sum with each other number. But it would O(n^2)

        The other approach is to use hash maps (dictionaries). I can 
        iterate the array and calculate its complement to achieve the target.
        So I consult the hash map (dictionary) to know if we already
        have that number (key) and its index (value). It would O(n) because
        I have to iterate the array, and the access to hash map is O(1).

        [PSUEDOCODE]
        - Initialize the hash map (dictionary)
        - Iterate the array
        - Calculate the complement
        - Check the dictionary
        - If the complement is not in the dictionary
          then save the number (key: value; index: number)
        - If it is in the dictionary, return the array starting
          with the smaller index.
        """
        
        seen_numbers = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen_numbers:
                return [seen_numbers[complement], i]
            else:
                seen_numbers[num] = i