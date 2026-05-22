class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        freq_arr = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            freqs[num] = 1 + freqs.get(num, 0)

        for i, val in freqs.items():
            freq_arr[val].append(i)

        res = []

        for i in range(len(freq_arr) - 1, -1, -1):
            for val in freq_arr[i]:
                res.append(val)
                if len(res) == k:
                    return res