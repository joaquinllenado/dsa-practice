class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minVal = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                minVal = min(minVal, nums[l])

            m = l + ((r - l) // 2)
            minVal = min(minVal, nums[m])
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        return minVal