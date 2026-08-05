class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_vals = {}

        for n in range(0, len(nums)):
            if (target - nums[n]) in seen_vals:
                return [seen_vals[target - nums[n]], n]
            else:
                seen_vals[nums[n]] = n
