class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0   

        longest = 0

        word_list = set()

        for end in range(len(s)):
            while s[end] in word_list:
                word_list.remove(s[start])
                start += 1
            
            word_list.add(s[end])
            longest = max(longest, end - start + 1)
                



        return longest