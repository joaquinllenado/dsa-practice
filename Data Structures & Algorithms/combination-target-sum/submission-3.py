class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, combos = [], []

        def backtrack(i = 0, cur_sum = 0):
            if cur_sum == target:
                res.append(combos[:])
                return
            if cur_sum > target or i >= len(nums):
                return
            
            combos.append(nums[i])
            backtrack(i, cur_sum + nums[i])
            combos.pop()
            backtrack(i + 1, cur_sum)
        
        backtrack()
        return res