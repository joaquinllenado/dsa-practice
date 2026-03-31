class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minEatingSpeed = r

        while l <= r:
            m = l + ((r - l) // 2)
            hours = 0

            for bananas in piles:
                hours += math.ceil(bananas / m)
            
            if hours <= h:
                minEatingSpeed = min(minEatingSpeed, m)
                r = m - 1
            else:
                l = m + 1
        return minEatingSpeed