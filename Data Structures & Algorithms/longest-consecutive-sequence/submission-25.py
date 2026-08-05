class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        
        seen = set(nums)

        for num in seen:
            if num - 1 not in seen:
                seq = 1
                cur = num + 1
                while cur in seen:
                    cur += 1
                    seq += 1
                
                longest= max(seq, longest)

        return longest 