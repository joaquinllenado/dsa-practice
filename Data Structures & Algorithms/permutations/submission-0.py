class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, combo = [], []

        def backtrack():
            if len(combo) == len(nums):
                res.append(combo[:])
                return
            
            for num in nums:
                if num not in combo:
                    combo.append(num)
                    backtrack()
                    combo.pop()
        
        backtrack()
        return res