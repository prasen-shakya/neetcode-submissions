class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water  = 0


        for l in range(len(heights)):
            for r in range(l + 1, len(heights)):
                water_area = (r - l) * min(heights[r], heights[l])

                max_water = max(water_area, max_water)

        return max_water