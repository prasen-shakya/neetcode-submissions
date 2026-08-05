class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_vals = {}

        for i in range(0, len(nums)):
            if target - nums[i] in seen_vals:
                return [seen_vals[target - nums[i]], i]
            
            seen_vals[nums[i]] = i