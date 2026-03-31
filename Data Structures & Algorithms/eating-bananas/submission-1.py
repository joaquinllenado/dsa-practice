class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minVal = r
        while l <= r:
            m = (l + r) // 2
            hours = 0
            for b in piles:
                hours += math.ceil(b / m)
            if hours <= h:
                minVal = min(minVal, m)
                r = m - 1
            else:
                l = m + 1
        return minVal