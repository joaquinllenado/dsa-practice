class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        for i, num in counts.items():
            freq[num].append(i)
        
        res = []

        for i in range(len(freq) - 1, -1, -1):
            for val in freq[i]:
                res.append(val)

                if len(res) == k:
                    return res