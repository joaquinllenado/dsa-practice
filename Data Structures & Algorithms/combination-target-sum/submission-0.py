class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, combo = [], []

        def backtrack(i, curSum):
            if curSum == target:
                res.append(combo[:])
                return
            
            if curSum > target or i >= len(nums):
                return
            
            combo.append(nums[i])
            backtrack(i, curSum + nums[i])

            combo.pop()
            backtrack(i + 1, curSum)
        
        backtrack(0,0)
        return res