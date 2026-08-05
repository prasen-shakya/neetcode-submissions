class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        unique_nums = set(nums)

        for num in unique_nums:
            cur_longest = 1

            next_num = num + 1

            while next_num in unique_nums:
                cur_longest += 1
                next_num = next_num + 1

            longest = max(longest, cur_longest)


        return longest


    