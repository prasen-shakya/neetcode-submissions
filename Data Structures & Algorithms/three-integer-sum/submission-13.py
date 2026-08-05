class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        seen = set()

        res = []

        for j in range(len(nums)):
            for i in range(len(nums) - 2):
                l = i + 1
                r = len(nums) - 1

                while l < r: 
                    total = nums[i] + nums[l] + nums[r]

                    tup = (nums[i], nums[l], nums[r])
                    if total == 0 and tup not in seen:
                        res.append([nums[i], nums[l], nums[r]])
                        seen.add(tup)
                    elif total < 0:
                        l += 1
                    else:
                        r -= 1
                
            return res