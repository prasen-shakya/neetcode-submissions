class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        res = [0] * len(nums)

        for idx in range(len(nums)):
            if idx == 0:
                prefix[idx] = nums[idx]
                continue
            
            prefix[idx] = prefix[idx - 1] * nums[idx]
        
        for idx in range(len(nums) - 1, -1, -1):
            if idx == len(nums) - 1:
                postfix[idx] = nums[idx]
                continue
            
            postfix[idx] = postfix[idx + 1] * nums[idx]
        
        for idx in range(len(nums)):
            if idx == 0:
                res[idx] = 1 * postfix[idx + 1]
            elif idx == len(nums) - 1:
                res[idx] = 1 * prefix[idx - 1]
            else:
                res[idx] = prefix[idx - 1] * postfix[idx + 1]

        return res