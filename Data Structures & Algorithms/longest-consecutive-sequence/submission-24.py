class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        avail_nums = set(nums)
        longest = 0

        for num in nums:
            cur = num
            count = 1

            if cur + 1  in avail_nums:
                continue 
            while cur - 1 in avail_nums:
                count += 1
                cur -= 1

            longest = max(count, longest)

                

        return longest