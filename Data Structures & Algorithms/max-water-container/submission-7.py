class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        l, r = 0, len(heights) - 1

        while l < r:
            min_height = min(heights[l], heights[r])
            cur_water = min_height * (r - l)
            max_water = max(max_water, cur_water)

            if min_height == heights[l]:
                l += 1
            else:
                r -= 1
        
        return max_water