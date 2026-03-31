class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        len_nums = len(nums) - 1

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue

            l, r = i + 1, len_nums
            while l < r:
                cur_sum = num + nums[l] + nums[r]

                if cur_sum == 0:
                    res.append([num, nums[l], nums[r]])
                    
                    l, r = l + 1, r - 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif cur_sum < 0:
                    l += 1
                else:
                    r -= 1
        
        return res