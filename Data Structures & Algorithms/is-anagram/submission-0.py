class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for i in s:
            if i not in s_dict:
                s_dict[i] = 1
            else:
                counter = s_dict[i]
                s_dict[i] = counter + 1
        for i in t:
            if i not in t_dict:
                t_dict[i] = 1
            else:
                counter = t_dict[i]
                t_dict[i] = counter + 1
        return s_dict == t_dict