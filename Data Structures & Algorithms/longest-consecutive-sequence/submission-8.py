class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0


        nums = sorted(set(nums))

        longest = 1
        print(nums)

        temp_longest = 1

        l, r = 0, 1
        while l != len(nums) - 1:
            if r == len(nums):
                longest = max(temp_longest, longest)
                break

            if nums[r] - nums[l] == r - l:
                temp_longest += 1
                print("adding", temp_longest)
            else:
                l = r
                longest = max(temp_longest, longest)
                temp_longest = 1
            
            r += 1
        
        print(longest)
        
        return longest



