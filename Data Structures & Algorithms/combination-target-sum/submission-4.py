class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, combos = [], []

        def backtrack(i = 0, current_sum = 0):
            if current_sum == target:
                res.append(combos[:])
                return
            if current_sum > target or i >= len(nums):
                return
            
            combos.append(nums[i])
            backtrack(i, current_sum + nums[i])

            combos.pop()
            backtrack(i + 1, current_sum)
        
        backtrack()

        return res