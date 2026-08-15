class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = 0

        def can_finish(speed):
            time = 0

            for p in piles:
                time += math.ceil(p / speed)
            
            return time <= h

        while l <= r:
            k = l + (r - l) // 2

            if can_finish(k):
                res = k
                r = k - 1
            else:
                l = k + 1
        
        return res
