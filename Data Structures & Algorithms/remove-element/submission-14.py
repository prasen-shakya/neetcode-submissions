class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0 
        r = len(nums) - 1

        while r > 0 and nums[r] == val:
            r -= 1

        while l <= r:
            if nums[l] == val:
                nums[l] = nums[r]
                r -= 1
                continue
                
            l += 1
        
        return r + 1