class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest_substring = 0

        chars = {}
        max_f = 0

        cur_size = 0

        l = 0

        for r in range(len(s)):
            chars[s[r]] = chars.get(s[r], 0) + 1

            print(s[r], ": ", chars[s[r]])

            max_f = max(max_f, chars[s[r]])
            print(l, r, max_f)
            if (r - l + 1) - max_f > k:
                print("HERE")
                chars[s[l]] -= 1
                l += 1
                cur_size = r - l + 1  # Update cur_size after moving l
            else:
                cur_size += 1
                longest_substring = max(cur_size, longest_substring)

        

        return longest_substring
