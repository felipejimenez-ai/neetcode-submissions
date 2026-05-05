from collections import defaultdict
from itertools import count
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      """
      Count the frequency.
      - Iterate the array.
      - Use a dictionary.

      Organize by highest frequency.
      - Take the dictonary to a list.
      - The list indexes represent the frequency.
        - E.g. index 0 is zero frequency.

      Return top k highest frequency.
      - Return the top k highest frequency.
      """

      frequency = defaultdict(int)
      for n in nums:
        frequency[n] += 1

      frequency_sorted = [[] for _ in range(len(nums) + 1)]
      for number, freq in frequency.items():
        frequency_sorted[freq].append(number)

      result = []
      for i in range(len(frequency_sorted) - 1, 0, -1):
        if frequency_sorted[i]:
          for j in frequency_sorted[i]:
            result.append(j)
            if len(result) == k:
              return result