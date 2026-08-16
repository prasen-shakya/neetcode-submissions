import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined_arrs = sorted(nums1 + nums2)

        med = (len(combined_arrs) - 1)/ 2
        
        if med % 1 != 0:
            return (combined_arrs[math.floor(med)] + combined_arrs[math.ceil(med)]) / 2
        
        return combined_arrs[int(med)]