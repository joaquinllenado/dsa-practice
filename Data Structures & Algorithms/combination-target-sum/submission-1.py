class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, combos = [], []

        def backtrack(i, curSum):
            if curSum == target:
                res.append(combos[:])
                return

            if curSum > target or i >= len(nums):
                return

            combos.append(nums[i])
            backtrack(i, curSum + nums[i])

            combos.pop()
            backtrack(i+1, curSum)
        
        backtrack(0, 0)
        return res