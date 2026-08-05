class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        # calculate prefix
        prefix = 1
        for idx in range(len(nums)):
            res[idx] = prefix
            prefix *= nums[idx]
        
        # calculate postfix
        postfix = 1
        for idx in range(len(nums) - 1, -1, -1):
            res[idx] *= postfix
            postfix *= nums[idx]
        
        return res