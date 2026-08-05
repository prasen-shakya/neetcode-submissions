class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_map = {}

        for x in range(len(nums)):
            if nums[x] in complement_map:
                print(complement_map)

                return [complement_map[nums[x]], x]
            complement = target - nums[x]
            complement_map[complement] = x
        