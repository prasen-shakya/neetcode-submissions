class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        
        smallest = 0

        while start <= end:
            mid = (start + end) // 2

            smallest = mid

            if nums[start] > nums[end]:
                start += 1
            else:
                end -= 1

        return nums[smallest]