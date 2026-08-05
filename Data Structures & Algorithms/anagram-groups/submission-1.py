class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}
        output = []

        for i in strs:
            if ''.join(sorted(i)) in anagram_groups.keys():
                anagram_groups[''.join(sorted(i))].append(i)
            else:
                anagram_groups[''.join(sorted(i))] = [i]
            
        for i in anagram_groups.values():
            output.append(i)
        
        return output

