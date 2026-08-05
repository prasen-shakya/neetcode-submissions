from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0
        max_length = 0
        max_freq = 0
        count_map = defaultdict(int)

        for right in range(0, len(s)):
            count_map[s[right]] += 1
            max_freq = max(max_freq, count_map[s[right]])

            if (right - left + 1) - max_freq > k:
                count_map[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length



        