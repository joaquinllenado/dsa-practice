class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        sorted_nums = nums.sort()

        longest = cur = 1
        prev = nums[0]

        for num in nums:
            if num == prev:
                continue
            
            if num != prev + 1:
                cur = 0
            
            cur += 1
            longest = max(longest, cur)
            prev = num
            # -1,-1,0,1,3,4,5,6,7,8,9
        
        return longest