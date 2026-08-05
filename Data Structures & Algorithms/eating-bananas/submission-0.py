class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(bph: int) -> bool:
            hour = 0
            for pile in piles:
                hour += math.ceil(pile / bph)
                if hour > h:
                    return False
            return True


        k = 1

        l, r = 1, max(piles)

        while(l <= r):
            mid = (l + r) // 2

            if (can_finish(mid)):
                k = mid
                r = mid - 1
            else:
                l = mid + 1


        return k