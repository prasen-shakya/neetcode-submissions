class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_map = {}

        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word in group_map:
                group_map[sorted_word].append(word)
            else:
                group_map[sorted_word] = [word]

        print(group_map.values())
        return group_map.values()