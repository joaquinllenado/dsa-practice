class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                cur = num + nums[l] + nums[r]

                if cur == 0:
                    res.append([num, nums[l], nums[r]])
                    l, r = l + 1, r - 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif cur < 0:
                    l += 1
                else:
                    r -= 1
        
        return res