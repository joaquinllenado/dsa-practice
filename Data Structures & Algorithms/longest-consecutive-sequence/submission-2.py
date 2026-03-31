class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        countSeq = 0
        seq = set(nums)

        for num in seq:
            if (num - 1) not in seq:
                length = 1
                while (num + length) in seq:
                    length += 1
                countSeq = max(length, countSeq)
        
        return countSeq