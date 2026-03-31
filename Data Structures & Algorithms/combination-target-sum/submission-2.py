class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, combinations = [], []

        def backtrack(i = 0, cur_sum = 0):
            if cur_sum == target:
                res.append(combinations[:])
                return

            if cur_sum > target or i >= len(nums):
                return

            combinations.append(nums[i])
            backtrack(i, cur_sum + nums[i])

            combinations.pop()
            backtrack(i + 1, cur_sum)
        
        backtrack()
        return res