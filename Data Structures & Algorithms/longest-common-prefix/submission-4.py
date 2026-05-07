class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        rslt = ''
        for i in range(len(strs[0])):
            for str in strs:
                if i == len(str) or str[i] != strs[0][i]:
                    return rslt
            rslt += strs[0][i]
        return rslt