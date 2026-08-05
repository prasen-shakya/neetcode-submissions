class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # {difference: index}
        difference_map = {}

        for i in range(0, len(nums)):
            difference = target - nums[i]
            if nums[i] in difference_map:
                return [difference_map[nums[i]], i]
            
            difference_map[difference] = i
        


