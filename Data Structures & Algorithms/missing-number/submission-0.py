class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        K = len(nums) + 1

        for x in range(K):
            res ^= x

        for num in nums:
            res ^= num
        
        return res