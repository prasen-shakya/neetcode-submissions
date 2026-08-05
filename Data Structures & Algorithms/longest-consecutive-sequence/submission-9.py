class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = set(nums)
        longest = 1

        for i in nums:
            length = 1

            cum_num = i
            while cum_num + 1 in nums:
                cum_num += 1
                length += 1
            
            longest = max(longest, length)



        return longest



