class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         numOccurance = {}
         
         for n in nums:
            if numOccurance.get(n):
                return True
            else:
                numOccurance[n] = 1

         return False