class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ""

        shortest_str = 0

        for i in range(len(strs)):
            if len(strs[i]) < len(strs[shortest_str]):
                shortest_str = i

        for i in range(len(strs[shortest_str])):
            for s in range(len(strs)):
                if strs[s][i] != strs[0][i]:
                    return longest
                
            longest += strs[0][i]
            

        return longest