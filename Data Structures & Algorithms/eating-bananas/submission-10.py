class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        def can_finish(speed):
            total_hours = 0

            for pile in piles:
                total_hours += math.ceil(pile / speed)

            return total_hours <= h

        while l < r:
            mid = (l + r) // 2

            if can_finish(mid):
                r = mid
            else:
                l = mid + 1

        return r