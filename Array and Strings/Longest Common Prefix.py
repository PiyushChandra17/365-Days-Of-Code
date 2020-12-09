class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        for z in zip(*strs):
            if len(set(z))==1:
                prefix += z[0]
            else:
                break
        return prefix