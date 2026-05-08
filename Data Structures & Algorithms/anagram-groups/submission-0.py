class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        for str in strs:
            str_sorted = ''.join(sorted(str))
            print(str)
            if str_sorted in words.keys():
                print(str)
                words[str_sorted].append(str)
            else:
                words[str_sorted] = [str]
        result = []
        for items in words.values():
            result.append(items)
        return result