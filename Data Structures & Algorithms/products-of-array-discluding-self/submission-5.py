class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        
        for i in range(len(nums)):
            prod = 1
            for k in range(len(nums)):
                if k == i:
                    continue
                prod *= nums[k]
            res.append(prod)

        return res