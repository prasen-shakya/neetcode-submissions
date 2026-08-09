class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = 1
        maj = nums[0]

        for num in nums:
            if num == maj:
                freq += 1
                continue
            
            freq -= 1

            if freq <= 0:
                maj = num
        
        return maj