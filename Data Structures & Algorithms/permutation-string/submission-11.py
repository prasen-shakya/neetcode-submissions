class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = {}
        s2_map = {}

        # Build s1_map
        for char in s1:
            s1_map[char] = s1_map.get(char, 0) + 1
        
        l = 0

        for r in range(len(s2)):
            s2_map[s2[r]] = s2_map.get(s2[r], 0) + 1

            if (r - l + 1) != len(s1):
                continue
            
            if s2_map == s1_map:
                return True
            
            s2_map[s2[l]] -= 1
            if s2_map[s2[l]] == 0:
                del s2_map[s2[l]]
            l += 1


        return False
