from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict_s = defaultdict(int)
        dict_t = defaultdict(int)

        for c in range(len(s)):
            dict_s[s[c]] += 1
            dict_t[t[c]] += 1
        
        return dict_s == dict_t