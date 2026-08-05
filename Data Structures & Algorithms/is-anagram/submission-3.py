class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_string_1 = {}
        hash_string_2 = {}

        for k in s:
            hash_string_1[k] = hash_string_1.get(k, 0) + 1

        for k in t:
            hash_string_2[k] = hash_string_2.get(k, 0) + 1
            
        return hash_string_1 == hash_string_2