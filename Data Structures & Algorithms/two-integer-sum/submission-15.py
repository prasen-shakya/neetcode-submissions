class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_values = {}

        for i in range(len(nums)):
            dif = target - nums[i]

            if dif in seen_values.keys():
                return [seen_values[dif], i]
            else:
                seen_values[nums[i]] = i
