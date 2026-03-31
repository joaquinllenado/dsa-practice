class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, subset = [], []

        def backtrack(i = 0):
            if i >= len(nums):
                res.append(subset[:])
                return
            
            subset.append(nums[i])
            backtrack(i + 1)

            subset.pop()
            backtrack(i + 1)
        
        backtrack()

        return res