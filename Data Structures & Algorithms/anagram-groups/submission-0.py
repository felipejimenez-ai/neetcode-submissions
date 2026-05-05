from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        * Initialize a dictionary 
        * Iterate the input list of words
        * Key -> Will be the organized character's word 
        * Value -> Will be the list of words
        * Check if the organized characters' word are already in the dict
        * Return the dictionary's values --list of words
        """
        
        anagrams = defaultdict(list)

        for w in strs:
            w_sorted = ''.join(sorted(w))
            anagrams[w_sorted].append(w)

        return list(anagrams.values())