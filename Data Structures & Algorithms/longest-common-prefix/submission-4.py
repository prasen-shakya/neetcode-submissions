class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ""


        for i in range(len(strs[0])):
            for s in range(1, len(strs)):
                if i == len(strs[s]) or strs[s][i] != strs[0][i]:
                    return longest
                
            longest += strs[0][i]
            

        return longest