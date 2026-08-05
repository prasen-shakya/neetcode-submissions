class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_arr = []
        output = []

        seen = []

        for i in strs:
            sorted_arr.append(''.join(sorted(i)))
        
        for x in range(len(strs)):
            if sorted_arr[x] in seen:
                continue
            
            similar_group = []
            similar_group.append(strs[x])
            seen.append(sorted_arr[x])


            for y in range(x + 1, len(strs)):
                if sorted_arr[x] == sorted_arr[y]:
                    similar_group.append(strs[y])
            
            output.append(similar_group)
        
        return output
