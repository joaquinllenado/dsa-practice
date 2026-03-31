class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const count = {};
        let freq = Array.from({ length: nums.length + 1 }, () => []);

        for (let num of nums){
            count[num] = 1 + (count[num] || 0);
        }

        for (let i in count) {
            freq[count[i]].push(Number(i));
        }

        let ans = [];

        for (let i = freq.length-1; i > 0; i--) {
            for (let j of freq[i]) {
                ans.push(j);
                if (ans.length === k){
                    return ans;
                }
            }
        }
    }
}
