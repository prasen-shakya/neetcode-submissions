class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         numOccurance = set()
         
         for n in nums:
            if n in numOccurance:
                return True
            else:
                numOccurance.add(n)

         return False