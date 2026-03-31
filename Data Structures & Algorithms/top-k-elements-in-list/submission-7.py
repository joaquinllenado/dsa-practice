class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        freq_array = [[] for i in range(len(nums) + 1)]

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        for key, val in freq.items():
            freq_array[val].append(key)

        res = []

        for i in range(len(freq_array) - 1, -1, -1):
            for j in range(len(freq_array[i])):
                res.append(freq_array[i][j])
                if len(res) == k:
                    return res